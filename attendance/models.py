from django.db import models
from members.models import Member


class Attendance(models.Model):
    ZONE_CHOICES = [
        ('main_hall', 'Main Hall'),
        ('zone_b', 'Zone B'),
        ('yoga_room', 'Yoga Room'),
        ('cardio_zone', 'Cardio Zone'),
        ('weight_room', 'Weight Room'),
        ('pool', 'Pool'),
        ('spa', 'Spa'),
    ]

    ACTIVITY_CHOICES = [
        ('general', 'General Training'),
        ('yoga', 'Yoga'),
        ('hiit', 'HIIT'),
        ('cardio', 'Cardio Blast'),
        ('powerlifting', 'Powerlifting'),
        ('crossfit', 'CrossFit'),
        ('leg_day', 'Leg Day'),
        ('upper_body', 'Upper Body'),
        ('personal_training', 'Personal Training'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='attendance_set')
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    zone = models.CharField(max_length=30, choices=ZONE_CHOICES, default='main_hall')
    activity = models.CharField(max_length=30, choices=ACTIVITY_CHOICES, default='general')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-check_in']

    def __str__(self):
        return f"{self.member} — {self.check_in.strftime('%Y-%m-%d %H:%M')}"

    @property
    def is_active(self):
        return self.check_out is None

    def duration_minutes(self):
        if self.check_out:
            delta = self.check_out - self.check_in
            return int(delta.total_seconds() / 60)
        return None
