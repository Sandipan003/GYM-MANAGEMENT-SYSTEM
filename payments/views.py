from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Sum
from django.utils import timezone
from .models import Payment
from .forms import PaymentForm
from members.models import Member


@login_required
def payment_list(request):
    payments = Payment.objects.select_related('member', 'plan').all()

    member_filter = request.GET.get('member', '')
    if member_filter:
        payments = payments.filter(member__id=member_filter)

    status_filter = request.GET.get('status', '')
    if status_filter:
        payments = payments.filter(status=status_filter)

    paginator = Paginator(payments, 15)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Monthly revenue
    today = timezone.now().date()
    month_start = today.replace(day=1)
    monthly_total = Payment.objects.filter(
        payment_date__gte=month_start,
        status='paid'
    ).aggregate(total=Sum('amount'))['total'] or 0

    context = {
        'payments': page_obj,
        'monthly_total': monthly_total,
        'member_filter': member_filter,
        'status_filter': status_filter,
        'page': 'payments',
    }
    return render(request, 'payments/list.html', context)


@login_required
def payment_add(request):
    member_id = request.GET.get('member')
    initial = {}
    if member_id:
        member = get_object_or_404(Member, pk=member_id)
        initial['member'] = member
        if member.plan:
            initial['plan'] = member.plan
            initial['amount'] = member.plan.price

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            # Update member status to active after successful payment
            if payment.status == 'paid':
                member = payment.member
                member.status = 'active'
                if payment.plan:
                    from datetime import date
                    from dateutil.relativedelta import relativedelta
                    try:
                        member.membership_expiry = date.today() + relativedelta(months=payment.plan.duration_months)
                    except Exception:
                        pass
                member.save()
            messages.success(request, f'Payment of ₹{payment.amount} recorded successfully!')
            return redirect('payment_list')
    else:
        form = PaymentForm(initial=initial)
        # Set today as default payment date
        form.initial['payment_date'] = timezone.now().date()

    context = {'form': form, 'page': 'payments'}
    return render(request, 'payments/form.html', context)
