from django.db import models


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
    photo = models.ImageField(upload_to='facilities/')
    capacity = models.PositiveIntegerField()
    features = models.TextField(help_text="Comma-separated features")
    operating_hours = models.CharField(max_length=100, default="6:00 AM - 11:00 PM")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['zone_type']
        verbose_name_plural = "Facilities"
    
    def __str__(self):
        return self.name
