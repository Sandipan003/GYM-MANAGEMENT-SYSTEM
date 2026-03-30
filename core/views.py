from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum, Count
from datetime import timedelta, date
import json

from members.models import Member
from payments.models import Payment
from attendance.models import Attendance


@login_required
def dashboard(request):
    today = timezone.now().date()
    now = timezone.now()
    month_start = today.replace(day=1)

    # Stat cards
    total_members = Member.objects.filter(status='active').count()
    monthly_revenue = Payment.objects.filter(
        payment_date__gte=month_start,
        status='paid'
    ).aggregate(total=Sum('amount'))['total'] or 0

    active_checkins = Attendance.objects.filter(
        check_in__date=today,
        check_out__isnull=True
    ).count()

    # Recent activity (last 10 attendance entries)
    recent_activity = Attendance.objects.select_related('member', 'member__plan').order_by('-check_in')[:10]

    # Revenue chart — last 6 months
    revenue_data = []
    labels = []
    for i in range(5, -1, -1):
        d = today - timedelta(days=i * 30)
        month_label = d.strftime('%b')
        month_rev = Payment.objects.filter(
            payment_date__year=d.year,
            payment_date__month=d.month,
            status='paid'
        ).aggregate(total=Sum('amount'))['total'] or 0
        revenue_data.append(float(month_rev))
        labels.append(month_label)

    max_rev = max(revenue_data) if revenue_data else 1

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
        'page': 'dashboard',
    }
    return render(request, 'core/dashboard.html', context)
