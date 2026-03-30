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

    # Search
    search = request.GET.get('search', '')
    if search:
        queryset = queryset.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search) |
            Q(member_id__icontains=search)
        )

    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        queryset = queryset.filter(status=status_filter)

    # Filter by plan
    plan_filter = request.GET.get('plan', '')
    if plan_filter:
        queryset = queryset.filter(plan__id=plan_filter)

    # Paginate
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page', 1)
    members = paginator.get_page(page_number)

    from plans.models import MembershipPlan
    plans = MembershipPlan.objects.filter(is_active=True)

    # Stats
    total_active = Member.objects.filter(status='active').count()

    context = {
        'members': members,
        'plans': plans,
        'search': search,
        'status_filter': status_filter,
        'plan_filter': plan_filter,
        'total_active': total_active,
        'page': 'members',
    }
    return render(request, 'members/list.html', context)


@login_required
def member_add(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save()
            messages.success(request, f'Member {member.get_full_name()} added successfully! ID: {member.member_id}')
            return redirect('member_list')
    else:
        form = MemberForm()

    context = {'form': form, 'action': 'Add', 'page': 'members'}
    return render(request, 'members/form.html', context)


@login_required
def member_edit(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member {member.get_full_name()} updated successfully!')
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)

    context = {'form': form, 'action': 'Edit', 'member': member, 'page': 'members'}
    return render(request, 'members/form.html', context)


@login_required
def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    payments = member.payments.all()[:10]
    attendance = member.attendance_set.all()[:10]

    context = {
        'member': member,
        'payments': payments,
        'attendance': attendance,
        'page': 'members',
    }
    return render(request, 'members/detail.html', context)


@login_required
def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        name = member.get_full_name()
        member.status = 'inactive'
        member.save()
        messages.success(request, f'Member {name} has been deactivated.')
        return redirect('member_list')
    return render(request, 'members/confirm_delete.html', {'member': member, 'page': 'members'})


@login_required
def member_dashboard(request):
    """Personal dashboard for gym members with real performance data"""
    if not hasattr(request.user, 'member_profile'):
        if request.user.is_staff:
            return redirect('staff')
        messages.error(request, 'No member profile found for this user.')
        return redirect('home')

    member = request.user.member_profile
    from attendance.models import Attendance
    
    # 1. Recent Activity
    recent_attendance = Attendance.objects.filter(member=member).order_by('-check_in')[:5]
    attendance_count = Attendance.objects.filter(member=member).count()

    # 2. Intensity Trends (Last 6 Months)
    now = timezone.now()
    six_months_ago = now - timedelta(days=180)
    monthly_trends_raw = Attendance.objects.filter(
        member=member, 
        check_in__gte=six_months_ago
    ).annotate(month=ExtractMonth('check_in')).values('month').annotate(count=Count('id')).order_by('month')
    
    # Convert to a stable list for the chart (padding months with 0)
    monthly_trends = []
    current_month = now.month
    for i in range(5, -1, -1):
        target_month = (current_month - i - 1) % 12 + 1
        count = next((item['count'] for item in monthly_trends_raw if item['month'] == target_month), 0)
        monthly_trends.append({'month': target_month, 'count': count})

    # 3. Weekly Pulse (Last 7 Days)
    weekly_pulse = []
    import datetime
    for i in range(6, -1, -1):
        day = (now - timedelta(days=i)).date()
        # Get range for the specific day (Bypass MySQL __date issues)
        start = timezone.make_aware(datetime.datetime.combine(day, datetime.time.min))
        end = timezone.make_aware(datetime.datetime.combine(day, datetime.time.max))
        has_attended = Attendance.objects.filter(member=member, check_in__range=(start, end)).exists()
        weekly_pulse.append(has_attended)

    # 4. Calories Burned (Est. 7.5 kcal/min)
    total_minutes = 0
    all_attendance = Attendance.objects.filter(member=member, check_out__isnull=False)
    for att in all_attendance:
        total_minutes += att.duration_minutes()
    calories_burned = total_minutes * 7.5

    # Calculate SVG Path for the Intensity Trends Chart
    # We'll use 6 points: (0, p1), (160, p2), (320, p3), (480, p4), (640, p5), (800, p6)
    # Height is 200. We'll map count=0 to y=180 and scale each visit as -15px (max 12 visits = y=0)
    points = []
    for i, trend in enumerate(monthly_trends):
        x = i * 160
        y = max(20, 180 - (trend['count'] * 15))
        points.append(f"{x},{y}")
    
    svg_points = " ".join(points)
    # Create the smooth cubic bezier path
    # For 6 points, we'll just join them or use a simple line for now, 
    # but the current template uses a Q/T path. Let's do a simple L path first for accuracy.
    svg_path = f"M {points[0]} " + " ".join([f"L {p}" for p in points[1:]])
    svg_fill = svg_path + " V 200 H 0 Z"

    # 5. Active Session Tracking
    active_session = Attendance.objects.filter(member=member, check_out__isnull=True).first()

    context = {
        'member': member,
        'recent_attendance': recent_attendance,
        'attendance_count': attendance_count,
        'monthly_trends': monthly_trends,
        'weekly_pulse': weekly_pulse,
        'calories_burned': int(calories_burned),
        'svg_points': svg_points,
        'svg_path': svg_path,
        'svg_fill': svg_fill,
        'last_point_y': points[-1].split(',')[1],
        'active_session': active_session,
        'page': 'member_dashboard',
    }
    return render(request, 'members/member_dashboard.html', context)


@login_required
def member_attendance_history(request):
    """Full attendance history for the member"""
    if not hasattr(request.user, 'member_profile'):
        return redirect('home')
    
    member = request.user.member_profile
    from attendance.models import Attendance
    queryset = Attendance.objects.filter(member=member).order_by('-check_in')
    
    paginator = Paginator(queryset, 15)
    page_number = request.GET.get('page')
    attendance_list = paginator.get_page(page_number)
    
    context = {
        'member': member,
        'attendance_list': attendance_list,
        'page': 'performance', # Highlight performance in sidebar
    }
    return render(request, 'members/attendance_history.html', context)


@login_required
def toggle_attendance(request):
    """Allow member to check-in or check-out themselves"""
    if not hasattr(request.user, 'member_profile'):
        messages.error(request, 'No member profile found.')
        return redirect('home')
    
    member = request.user.member_profile
    from attendance.models import Attendance
    
    active_session = Attendance.objects.filter(member=member, check_out__isnull=True).first()
    
    if request.method == 'POST':
        if active_session:
            active_session.check_out = timezone.now()
            active_session.save()
            messages.success(request, 'Great session! You have been checked out.')
        else:
            # Create new check-in
            Attendance.objects.create(
                member=member,
                check_in=timezone.now(),
                zone='main_hall',
                activity='general'
            )
            messages.success(request, 'Welcome to Kinetic Pulse! Your session has started.')
            
    return redirect('member_dashboard')
