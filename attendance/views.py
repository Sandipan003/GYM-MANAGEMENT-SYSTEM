from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count
from .models import Attendance
from .forms import AttendanceCheckInForm
from members.models import Member


@login_required
def attendance_reports(request):
    today = timezone.now().date()
    now = timezone.now()

    # Today's check-ins
    todays_checkins = Attendance.objects.filter(
        check_in__date=today
    ).select_related('member', 'member__plan').order_by('-check_in')[:20]

    # Currently active (checked in, not checked out)
    active_now = Attendance.objects.filter(
        check_in__date=today,
        check_out__isnull=True
    ).count()

    # Peak hours — aggregate check-ins by hour (today or last 7 days)
    from django.db.models.functions import ExtractHour
    from datetime import timedelta

    week_ago = today - timedelta(days=7)
    hourly_data = (
        Attendance.objects
        .filter(check_in__date__gte=week_ago)
        .annotate(hour=ExtractHour('check_in'))
        .values('hour')
        .annotate(count=Count('id'))
        .order_by('hour')
    )

    # Build hour slots 6am-10pm
    hour_counts = {item['hour']: item['count'] for item in hourly_data}
    hours_range = range(6, 23, 2)
    peak_hours = []
    max_count = max(hour_counts.values()) if hour_counts else 1
    for h in hours_range:
        count = hour_counts.get(h, 0)
        height = int((count / max_count) * 100) if max_count > 0 else 5
        peak_hours.append({
            'label': f'{h:02d}:00',
            'count': count,
            'height': max(height, 5),
            'is_peak': height >= 90,
        })

    # Frequency split
    total_members = Member.objects.filter(status='active').count()
    daily_members = Member.objects.filter(
        attendance_set__check_in__date__gte=today - timedelta(days=7)
    ).distinct().count()

    weekly_members = Member.objects.filter(
        attendance_set__check_in__date__gte=today - timedelta(days=30)
    ).distinct().count()

    freq_daily = int((daily_members / total_members * 100)) if total_members else 0
    freq_weekly = int(((weekly_members - daily_members) / total_members * 100)) if total_members > 0 else 0
    freq_occasional = max(0, 100 - freq_daily - freq_weekly)

    context = {
        'todays_checkins': todays_checkins,
        'active_now': active_now,
        'peak_hours': peak_hours,
        'total_members': total_members,
        'freq_daily': freq_daily,
        'freq_weekly': freq_weekly,
        'freq_occasional': freq_occasional,
        'today': today,
        'page': 'attendance',
    }
    return render(request, 'attendance/reports.html', context)


@login_required
def checkin(request):
    if request.method == 'POST':
        form = AttendanceCheckInForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.check_in = timezone.now()
            attendance.save()
            messages.success(request, f'{attendance.member.get_full_name()} checked in successfully!')
            return redirect('attendance_reports')
    else:
        form = AttendanceCheckInForm()

    context = {'form': form, 'page': 'attendance'}
    return render(request, 'attendance/checkin.html', context)


@login_required
def checkout(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk, check_out__isnull=True)
    attendance.check_out = timezone.now()
    attendance.save()
    messages.success(request, f'{attendance.member.get_full_name()} checked out successfully!')
    return redirect('attendance_reports')
