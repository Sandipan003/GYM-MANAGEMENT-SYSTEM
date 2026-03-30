from django.contrib import admin
from .models import MembershipPlan


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration_months', 'is_featured', 'is_active']
    list_filter = ['is_featured', 'is_active']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
