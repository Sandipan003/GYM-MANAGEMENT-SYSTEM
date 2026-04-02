from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Equipment(models.Model):
    """Gym equipment with photo and details"""
    CATEGORY_CHOICES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength Training'),
        ('flexibility', 'Flexibility'),
        ('functional', 'Functional Training'),
        ('recovery', 'Recovery'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    photo = models.ImageField(upload_to='equipment/', blank=True, null=True)
    specifications = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=20, 
        choices=[('active', 'Active'), ('maintenance', 'Maintenance'), ('inactive', 'Inactive')],
        default='active'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category', 'name']
    
    def __str__(self):
        return self.name


class Facility(models.Model):
    """Gym facility/zone with details"""
    ZONE_TYPES = [
        ('cardio', 'Cardio Zone'),
        ('weights', 'Weight Training'),
        ('functional', 'Functional Area'),
        ('yoga', 'Yoga & Stretching'),
        ('locker', 'Locker Room'),
        ('pool', 'Pool Area'),
        ('studio', 'Studio'),
    ]
    
    name = models.CharField(max_length=100)
    zone_type = models.CharField(max_length=20, choices=ZONE_TYPES)
    description = models.TextField()
    photo = models.ImageField(upload_to='facilities/', blank=True, null=True)
    capacity = models.PositiveIntegerField()
    features = models.TextField(help_text="Comma-separated features")
    operating_hours = models.CharField(max_length=100, default="6:00 AM - 11:00 PM")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['zone_type']
        verbose_name_plural = "Facilities"
    
    def __str__(self):
        return self.name

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    photo = models.ImageField(upload_to='staff/', blank=True, null=True)
    bio = models.TextField(blank=True, max_length=500)
    
    def __str__(self):
        return f"Profile - {self.user.username}"

@receiver(post_save, sender=User)
def create_staff_profile(sender, instance, created, **kwargs):
    if created and instance.is_staff:
        StaffProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_staff_profile(sender, instance, **kwargs):
    if instance.is_staff:
        if hasattr(instance, 'staff_profile'):
            instance.staff_profile.save()
        else:
            StaffProfile.objects.get_or_create(user=instance)
