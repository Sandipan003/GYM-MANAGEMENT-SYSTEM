from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum, Count
from datetime import timedelta, date
import json

from members.models import Member
from payments.models import Payment
from attendance.models import Attendance


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
    if request.user.is_staff:
        return redirect('staff')
    else:
        # Check if user has an associated member profile
        if hasattr(request.user, 'member_profile'):
            return redirect('member_dashboard')
        else:
            # If logged in but no member profile, just go home or admin
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
