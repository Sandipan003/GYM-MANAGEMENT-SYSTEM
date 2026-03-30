from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
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
