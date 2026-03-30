from django.db import models


class MembershipPlan(models.Model):
    COLOR_CHOICES = [
        ('primary', 'Primary (Yellow-Green)'),
        ('secondary', 'Secondary (Cyan)'),
        ('tertiary', 'Tertiary (Gold)'),
        ('outline', 'Outline (Gray)'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True)
    features = models.TextField(
        help_text="One feature per line",
        blank=True
    )
    is_featured = models.BooleanField(default=False)
    color_label = models.CharField(max_length=20, choices=COLOR_CHOICES, default='primary')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.name

    def get_features_list(self):
        return [f.strip() for f in self.features.splitlines() if f.strip()]
