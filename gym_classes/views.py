from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import GymClass, Enrollment
from .forms import GymClassForm
from django.contrib import messages

def is_staff(user):
    return user.is_staff

@login_required
def class_list(request):
    """View to list all gym classes for members"""
    if not hasattr(request.user, 'member_profile'):
        if request.user.is_staff:
            return redirect('staff_class_list')
        return redirect('home')
    
    member = request.user.member_profile
    classes = GymClass.objects.all().prefetch_related('enrolled_members')
    
    # Identify which classes the user is enrolled in
    user_enrolled_classes = []
    if request.user.is_authenticated:
        user_enrolled_classes = Enrollment.objects.filter(user=request.user).values_list('gym_class_id', flat=True)
    
    # Filter by day if requested
    day_filter = request.GET.get('day', '')
    if day_filter:
        classes = classes.filter(day=day_filter)
    
    # Enrich classes with current enrollment count and user status
    for cls in classes:
        cls.current_enrolled = cls.enrolled_members.count()
        cls.is_user_enrolled = cls.id in user_enrolled_classes
        cls.spots_remaining = max(0, cls.capacity - cls.current_enrolled)
    
    context = {
        'member': member,
        'classes': classes,
        'user_enrolled_classes': user_enrolled_classes,
        'day_filter': day_filter,
        'page': 'classes',
    }
    return render(request, 'gym_classes/list.html', context)

@login_required
def book_class(request, class_id):
    """Enroll a member in a gym class"""
    if request.method == 'POST':
        gym_class = get_object_or_404(GymClass, pk=class_id)
        
        # Check if already enrolled
        if Enrollment.objects.filter(user=request.user, gym_class=gym_class).exists():
            messages.warning(request, f'You are already enrolled in {gym_class.name}.')
            return redirect('class_list')
            
        # Check capacity
        if Enrollment.objects.filter(gym_class=gym_class).count() >= gym_class.capacity:
            messages.error(request, f'Sorry, {gym_class.name} is at full capacity.')
            return redirect('class_list')
            
        # Create enrollment
        Enrollment.objects.create(user=request.user, gym_class=gym_class)
        messages.success(request, f'Successfully enrolled in {gym_class.name}! See you there.')
        
    return redirect('class_list')

@login_required
def unbook_class(request, class_id):
    """Remove a member from a gym class enrollment"""
    if request.method == 'POST':
        gym_class = get_object_or_404(GymClass, pk=class_id)
        Enrollment.objects.filter(user=request.user, gym_class=gym_class).delete()
        messages.success(request, f'You have left {gym_class.name}.')
    return redirect('class_list')

# STAFF VIEWS (REMAIN UNCHANGED)
@user_passes_test(is_staff)
def staff_class_list(request):
    classes = GymClass.objects.all().order_by('day', 'start_time')
    return render(request, 'gym_classes/staff_list.html', {'classes': classes, 'page': 'classes'})

@user_passes_test(is_staff)
def staff_class_add(request):
    if request.method == 'POST':
        form = GymClassForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New class added successfully!')
            return redirect('staff_class_list')
    else:
        form = GymClassForm()
    return render(request, 'gym_classes/staff_form.html', {'form': form, 'page': 'classes', 'title': 'Add Class'})

@user_passes_test(is_staff)
def staff_class_edit(request, pk):
    gym_class = get_object_or_404(GymClass, pk=pk)
    if request.method == 'POST':
        form = GymClassForm(request.POST, request.FILES, instance=gym_class)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class updated!')
            return redirect('staff_class_list')
    else:
        form = GymClassForm(instance=gym_class)
    return render(request, 'gym_classes/staff_form.html', {'form': form, 'page': 'classes', 'title': 'Edit Class'})

@user_passes_test(is_staff)
def staff_class_delete(request, pk):
    gym_class = get_object_or_404(GymClass, pk=pk)
    if request.method == 'POST':
        gym_class.delete()
        messages.success(request, 'Class deleted!')
        return redirect('staff_class_list')
    return render(request, 'gym_classes/staff_delete.html', {'gym_class': gym_class})
