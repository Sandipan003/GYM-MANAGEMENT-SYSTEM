from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MembershipPlan
from .forms import PlanForm


@login_required
def plan_list(request):
    plans = MembershipPlan.objects.filter(is_active=True)
    context = {'plans': plans, 'page': 'plans'}
    return render(request, 'plans/list.html', context)


@login_required
def plan_add(request):
    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES)
        if form.is_valid():
            plan = form.save()
            messages.success(request, f'Plan "{plan.name}" created successfully!')
            return redirect('plan_list')
    else:
        form = PlanForm()

    context = {'form': form, 'action': 'Create', 'page': 'plans'}
    return render(request, 'plans/form.html', context)


@login_required
def plan_edit(request, pk):
    plan = get_object_or_404(MembershipPlan, pk=pk)
    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, f'Plan "{plan.name}" updated successfully!')
            return redirect('plan_list')
    else:
        form = PlanForm(instance=plan)

    context = {'form': form, 'action': 'Edit', 'plan': plan, 'page': 'plans'}
    return render(request, 'plans/form.html', context)


@login_required
def plan_delete(request, pk):
    plan = get_object_or_404(MembershipPlan, pk=pk)
    if request.method == 'POST':
        plan.is_active = False
        plan.save()
        messages.success(request, f'Plan "{plan.name}" has been deactivated.')
        return redirect('plan_list')
    return render(request, 'plans/confirm_delete.html', {'plan': plan, 'page': 'plans'})
