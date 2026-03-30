from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count
from datetime import timedelta
from .models import Attendance
from .forms import AttendanceCheckInForm
from members.models import Member
import datetime

def get_date_range(date_obj):
    """Returns a tuple of (start_datetime, end_datetime) for a given date, aware of current timezone."""
    start = timezone.make_aware(datetime.datetime.combine(date_obj, datetime.time.min))
    end = timezone.make_aware(datetime.datetime.combine(date_obj, datetime.time.max))
    return start, end

@login_required
def attendance_reports(request):
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    # Get ranges for precise filtering (Bypass MySQL __date issues)
    y_start, y_end = get_date_range(yesterday)
    t_start, t_end = get_date_range(today)
    tm_start, tm_end = get_date_range(tomorrow)

    # Yesterday's check-ins
    yesterdays_checkins = Attendance.objects.filter(
        check_in__range=(y_start, y_end)
    ).select_related('member', 'member__plan').order_by('-check_in')

    # Today's check-ins (Primary)
    todays_checkins = Attendance.objects.filter(
        check_in__range=(t_start, t_end)
    ).select_related('member', 'member__plan').order_by('-check_in')

    # Tomorrow's check-ins (Future/Planned if any)
    tomorrows_checkins = Attendance.objects.filter(
        check_in__range=(tm_start, tm_end)
    ).select_related('member', 'member__plan').order_by('-check_in')

    # Currently active (checked in, not checked out)
    active_now = Attendance.objects.filter(
        check_in__range=(t_start, t_end),
        check_out__isnull=True
    ).count()

    context = {
        'yesterdays_checkins': yesterdays_checkins,
        'todays_checkins': todays_checkins,
        'tomorrows_checkins': tomorrows_checkins,
        'yesterday': yesterday,
        'today': today,
        'tomorrow': tomorrow,
        'active_now': active_now,
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
