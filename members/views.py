from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum
from django.db.models.functions import ExtractMonth
from django.utils import timezone
from datetime import timedelta
from .models import Member
from .forms import MemberForm

@login_required
def member_list(request):
    queryset = Member.objects.select_related('plan').all()
    search = request.GET.get('search', '')
    if search:
        queryset = queryset.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search) |
            Q(member_id__icontains=search)
        )
    paginator = Paginator(queryset, 10)
    members = paginator.get_page(request.GET.get('page', 1))
    return render(request, 'members/list.html', {'members': members, 'page': 'members'})

@login_required
def member_add(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save()
            messages.success(request, f'Member {member.get_full_name()} added!')
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'members/form.html', {'form': form, 'action': 'Add', 'page': 'members'})

@login_required
def member_edit(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member updated!')
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/form.html', {'form': form, 'action': 'Edit', 'member': member, 'page': 'members'})

@login_required
def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'members/detail.html', {'member': member, 'page': 'members'})

@login_required
def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.status = 'inactive'
        member.save()
        messages.success(request, 'Member deactivated.')
        return redirect('member_list')
    return render(request, 'members/confirm_delete.html', {'member': member, 'page': 'members'})

@login_required
def member_dashboard(request):
    """Personal dashboard for gym members with real performance data"""
    if not hasattr(request.user, 'member_profile'):
        if request.user.is_staff:
            return redirect('staff')
        return redirect('home')

    member = request.user.member_profile
    from attendance.models import Attendance
    
    recent_attendance = Attendance.objects.filter(member=member).order_by('-check_in')[:5]
    attendance_count = Attendance.objects.filter(member=member).count()

    now = timezone.now()
    six_months_ago = now - timedelta(days=180)
    monthly_trends_raw = Attendance.objects.filter(member=member, check_in__gte=six_months_ago).annotate(month=ExtractMonth('check_in')).values('month').annotate(count=Count('id')).order_by('month')
    
    monthly_trends = []
    current_month = now.month
    for i in range(5, -1, -1):
        target_month = (current_month - i - 1) % 12 + 1
        count = next((item['count'] for item in monthly_trends_raw if item['month'] == target_month), 0)
        x_coord = (5 - i) * 160
        y_coord = max(20, 180 - (count * 15))
        monthly_trends.append({'month': target_month, 'count': count, 'x': x_coord, 'y': y_coord})

    weekly_pulse = []
    for i in range(6, -1, -1):
        day = (now - timedelta(days=i)).date()
        weekly_pulse.append(Attendance.objects.filter(member=member, check_in__date=day).exists())

    total_minutes = sum([a.duration_minutes() for a in Attendance.objects.filter(member=member, check_out__isnull=False)])
    calories_burned = total_minutes * 7.5

    points = [f"{t['x']},{t['y']}" for t in monthly_trends]
    svg_path = f"M {points[0]} " + " ".join([f"L {p}" for p in points[1:]])
    svg_fill = svg_path + " V 200 H 0 Z"

    active_session = Attendance.objects.filter(member=member, check_out__isnull=True).first()

    context = {
        'member': member,
        'recent_attendance': recent_attendance,
        'attendance_count': attendance_count,
        'monthly_trends': monthly_trends,
        'weekly_pulse': weekly_pulse,
        'calories_burned': int(calories_burned),
        'svg_path': svg_path,
        'svg_fill': svg_fill,
        'active_session': active_session,
        'page': 'member_dashboard',
    }
    return render(request, 'members/member_dashboard.html', context)

@login_required
def member_attendance_history(request):
    if not hasattr(request.user, 'member_profile'): return redirect('home')
    from attendance.models import Attendance
    attendance_list = Attendance.objects.filter(member=request.user.member_profile).order_by('-check_in')
    return render(request, 'members/attendance_history.html', {'attendance_list': attendance_list, 'page': 'performance'})

@login_required
def toggle_attendance(request):
    if not hasattr(request.user, 'member_profile'): return redirect('home')
    from attendance.models import Attendance
    active = Attendance.objects.filter(member=request.user.member_profile, check_out__isnull=True).first()
    if request.method == 'POST':
        if active:
            active.check_out = timezone.now()
            active.save()
        else:
            Attendance.objects.create(member=request.user.member_profile, check_in=timezone.now(), zone='main_hall')
    return redirect('member_dashboard')

@login_required
def member_plans(request):
    if not hasattr(request.user, 'member_profile'): return redirect('home')
    from plans.models import MembershipPlan
    plans = MembershipPlan.objects.filter(is_active=True).order_by('price')
    return render(request, 'members/plans.html', {'plans': plans, 'page': 'membership'})

@login_required
def process_plan_payment(request, plan_id):
    if not hasattr(request.user, 'member_profile'): return redirect('home')
    from plans.models import MembershipPlan
    from payments.models import Payment
    plan = get_object_or_404(MembershipPlan, pk=plan_id)
    if request.method == 'POST':
        Payment.objects.create(member=request.user.member_profile, plan=plan, amount=plan.price, status='paid')
        request.user.member_profile.plan = plan
        request.user.member_profile.status = 'active'
        request.user.member_profile.save()
        messages.success(request, f'Activated {plan.name} plan!')
    return redirect('member_dashboard')


from .forms import MemberSignupForm
from django.contrib.auth import login

def signup(request):
    if request.user.is_authenticated:
        return redirect('login_success')
        
    plan_id = request.GET.get('plan')
    initial_data = {}
    if plan_id:
        initial_data['plan'] = plan_id

    if request.method == 'POST':
        form = MemberSignupForm(request.POST)
        if form.is_valid():
            # Use transaction to ensure both user and member are created
            from django.db import transaction
            try:
                with transaction.atomic():
                    from django.contrib.auth.models import User
                    user = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password'],
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name']
                    )
                    
                    member = Member.objects.create(
                        user=user,
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        email=form.cleaned_data['email'],
                        phone=form.cleaned_data['phone'],
                        plan=form.cleaned_data['plan'],
                        join_date=timezone.now().date(),
                        status='active' # Auto-activate for demo
                    )
                    
                    # Log the user in
                    login(request, user)
                    messages.success(request, f"Welcome to KINETICA, {user.first_name}! Your {member.plan.name} membership is active.")
                    return redirect('member_dashboard')
            except Exception as e:
                messages.error(request, f"Error during registration: {str(e)}")
    else:
        form = MemberSignupForm(initial=initial_data)
        
    return render(request, 'members/signup.html', {'form': form})
