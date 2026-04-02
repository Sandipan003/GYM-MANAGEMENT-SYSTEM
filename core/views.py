from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.db.models import Sum, Count, Q
from django.contrib import messages
from datetime import timedelta, date
import json

from members.models import Member
from payments.models import Payment
from attendance.models import Attendance
from .models import Equipment, Facility, StaffProfile
from .forms import FacilityForm, EquipmentForm, UserUpdateForm, StaffProfileForm


def home(request):
    """Public landing page with live facility stats"""
    today = timezone.now().date()
    
    # Live activity (only check-ins without check-outs)
    live_activity = Attendance.objects.filter(
        check_out__isnull=True
    ).select_related('member')[:3]
    
    # Calculate occupancy (simulated based on active check-ins vs capacity of 50)
    active_count = Attendance.objects.filter(check_out__isnull=True).count()
    occupancy_percent = min(int((active_count / 50) * 100), 100)
    
    context = {
        'live_activity': live_activity,
        'occupancy_percent': occupancy_percent,
        'today': today,
    }
    return render(request, 'core/home.html', context)


@login_required
def login_success(request):
    """Redirect users to appropriate dashboard based on role"""
    import django.contrib.messages as messages
    
    if request.user.is_staff:
        return redirect('staff')
    else:
        # Check if user has an associated member profile
        if hasattr(request.user, 'member_profile'):
            return redirect('member_dashboard')
        else:
            # If logged in but no member profile, allow them to view home but inform them
            messages.info(request, f"Welcome, {request.user.username}. Note: No member profile is linked to your account yet. Please contact staff.")
            return redirect('home')


@login_required
def dashboard(request):
    """Staff Management Dashboard"""
    if not request.user.is_staff:
        return redirect('member_dashboard')
        
    today = timezone.now().date()
    # ... rest of existing dashboard logic ...
    today = timezone.now().date()
    now = timezone.now()
    month_start = today.replace(day=1)

    # Stat cards
    total_members = Member.objects.filter(status='active').count()
    monthly_revenue = Payment.objects.filter(
        payment_date__gte=month_start,
        status='paid'
    ).aggregate(total=Sum('amount'))['total'] or 0

    # Get range for today (Bypass MySQL __date issues)
    import datetime
    start = timezone.make_aware(datetime.datetime.combine(today, datetime.time.min))
    end = timezone.make_aware(datetime.datetime.combine(today, datetime.time.max))

    active_checkins = Attendance.objects.filter(
        check_in__range=(start, end),
        check_out__isnull=True
    ).count()

    # Recent activity (last 10 attendance entries)
    recent_activity = Attendance.objects.select_related('member', 'member__plan').order_by('-check_in')[:10]

    # Revenue chart — last 6 months (Robust calculation)
    revenue_data = []
    labels = []
    
    # Start from current month and go back 5 months
    curr_date = today.replace(day=1)
    temp_months = []
    for _ in range(6):
        rev = Payment.objects.filter(
            payment_date__year=curr_date.year,
            payment_date__month=curr_date.month,
            status='paid'
        ).aggregate(total=Sum('amount'))['total'] or 0
        
        temp_months.append({
            'label': curr_date.strftime('%b').upper(),
            'value': float(rev)
        })
        
        # Move to previous month: go to 1st of current month, subtract 1 day
        last_month = (curr_date - timedelta(days=1)).replace(day=1)
        curr_date = last_month

    # Reverse to show Oct -> Mar
    temp_months.reverse()
    revenue_data = [m['value'] for m in temp_months]
    labels = [m['label'] for m in temp_months]

    max_rev = max(revenue_data) if any(revenue_data) else 1

    # Build bar chart heights as percentages
    chart_bars = []
    for i, rev in enumerate(revenue_data):
        height = int((rev / max_rev) * 100) if max_rev > 0 else 10
        chart_bars.append({'label': labels[i], 'height': max(height, 5), 'value': rev})

    context = {
        'total_members': total_members,
        'monthly_revenue': monthly_revenue,
        'active_checkins': active_checkins,
        'recent_activity': recent_activity,
        'chart_bars': chart_bars,
        'today': today,
        'page': 'staff',
    }
    return render(request, 'core/dashboard.html', context)


def facility_view(request):
    """Facility showcase page"""
    facilities = Facility.objects.all()
    equipment_by_category = {}
    
    for equipment in Equipment.objects.filter(status='active'):
        category = equipment.get_category_display()
        if category not in equipment_by_category:
            equipment_by_category[category] = []
        equipment_by_category[category].append(equipment)
    
    context = {
        'facilities': facilities,
        'equipment_by_category': equipment_by_category,
    }
    return render(request, 'core/facility.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def facility_manage(request):
    """Admin: Manage Facilities and Equipment List"""
    facilities = Facility.objects.all()
    equipment_list = Equipment.objects.all()
    context = {
        'facilities': facilities,
        'equipment_list': equipment_list,
        'page': 'facility',
    }
    return render(request, 'core/admin/facility_list.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def facility_add(request):
    """Admin: Add Facility"""
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Facility added successfully!')
            return redirect('facility_manage')
    else:
        form = FacilityForm()
    
    return render(request, 'core/admin/facility_form.html', {'form': form, 'title': 'Create Facility'})

@login_required
@user_passes_test(lambda u: u.is_staff)
def facility_edit(request, pk):
    """Admin: Edit Facility"""
    facility = get_object_or_404(Facility, pk=pk)
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES, instance=facility)
        if form.is_valid():
            form.save()
            messages.success(request, 'Facility updated!')
            return redirect('facility_manage')
    else:
        form = FacilityForm(instance=facility)
    
    return render(request, 'core/admin/facility_form.html', {'form': form, 'title': 'Edit Facility'})

@login_required
@user_passes_test(lambda u: u.is_staff)
def facility_delete(request, pk):
    """Admin: Delete Facility"""
    facility = get_object_or_404(Facility, pk=pk)
    if request.method == 'POST':
        facility.delete()
        messages.success(request, 'Facility deleted.')
    return redirect('facility_manage')

# EQUIPMENT CRUD
@login_required
@user_passes_test(lambda u: u.is_staff)
def equipment_add(request):
    """Admin: Add Equipment"""
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipment Added!')
            return redirect('facility_manage')
    else:
        form = EquipmentForm()
    return render(request, 'core/admin/equipment_form.html', {'form': form, 'title': 'Add Equipment'})

@login_required
@user_passes_test(lambda u: u.is_staff)
def profile_settings(request):
    """Admin: Profile and Account Settings"""
    # Ensure profile exists
    profile, created = StaffProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = StaffProfileForm(request.POST, request.FILES, instance=profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile system updated successfully!')
            return redirect('profile_settings')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = StaffProfileForm(instance=profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Account Identity',
        'page': 'profile'
    }
    return render(request, 'core/admin/profile_settings.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def equipment_edit(request, pk):
    """Admin: Edit Equipment"""
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES, instance=equipment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipment Updated!')
            return redirect('facility_manage')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'core/admin/equipment_form.html', {'form': form, 'title': 'Edit Equipment'})

@login_required
@user_passes_test(lambda u: u.is_staff)
def equipment_delete(request, pk):
    """Admin: Delete Equipment"""
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        messages.success(request, 'Equipment Removed.')
    return redirect('facility_manage')

def metrics_view(request):
    """Metrics and analytics page"""
    today = timezone.now().date()
    now = timezone.now()
    month_start = today.replace(day=1)
    
    # Statistics
    total_members = Member.objects.filter(status='active').count()
    total_checkins_today = Attendance.objects.filter(check_in__date=today).count()
    monthly_revenue = Payment.objects.filter(
        payment_date__gte=month_start,
        status='paid'
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    # Active members today
    active_today = Attendance.objects.filter(
        check_out__isnull=True
    ).select_related('member').count()
    
    context = {
        'total_members': total_members,
        'total_checkins_today': total_checkins_today,
        'monthly_revenue': monthly_revenue,
        'active_today': active_today,
        'today': today,
    }
    return render(request, 'core/metrics.html', context)


def membership_view(request):
    """Membership and pricing page"""
    from plans.models import MembershipPlan
    plans = MembershipPlan.objects.filter(is_active=True)
    
    context = {
        'plans': plans,
    }
    return render(request, 'core/membership.html', context)
