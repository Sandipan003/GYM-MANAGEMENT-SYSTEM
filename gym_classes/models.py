from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class GymClass(models.Model):
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('elite', 'Elite'),
    ]

    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    description = models.TextField()
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    start_time = models.TimeField()
    duration_minutes = models.IntegerField(default=60)
    capacity = models.IntegerField(default=20)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='intermediate')
    icon = models.CharField(max_length=50, default='fitness_center')
    color_label = models.CharField(max_length=20, default='primary') # primary, secondary, tertiary
    photo = models.ImageField(upload_to='classes/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Gym Classes"
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"{self.name} with {self.instructor}"

    def end_time(self):
        # Implementation for convenience in templates
        from datetime import datetime, timedelta
        dummy_date = datetime.combine(timezone.now().date(), self.start_time)
        return (dummy_date + timedelta(minutes=self.duration_minutes)).time()

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='class_enrollments')
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE, related_name='enrolled_members')
    booked_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'gym_class')
        ordering = ['-booked_at']

    def __str__(self):
        return f"{self.user.username} enrolled in {self.gym_class.name}"
