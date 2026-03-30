from django.db import models
from plans.models import MembershipPlan


def member_photo_path(instance, filename):
    return f'members/{instance.member_id}/{filename}'


class Member(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('pending', 'Pending'),
        ('inactive', 'Inactive'),
    ]

    member_id = models.CharField(max_length=20, unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to=member_photo_path, null=True, blank=True)
    plan = models.ForeignKey(
        MembershipPlan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='members'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    join_date = models.DateField()
    membership_expiry = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    emergency_contact = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.member_id:
            # Auto-generate member ID like KP-0001
            super().save(*args, **kwargs)
            self.member_id = f"KP-{self.pk:04d}"
            Member.objects.filter(pk=self.pk).update(member_id=self.member_id)
        else:
            super().save(*args, **kwargs)

    @property
    def status_display(self):
        return self.get_status_display()

    def get_last_attendance(self):
        return self.attendance_set.order_by('-check_in').first()
