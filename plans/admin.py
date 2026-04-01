from django.contrib import admin
from .models import MembershipPlan


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration_months', 'is_featured', 'is_active', 'created_at']
    list_filter = ['is_featured', 'is_active', 'color_label', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description')
        }),
        ('Pricing & Duration', {
            'fields': ('price', 'duration_months')
        }),
        ('Features', {
            'fields': ('features',),
            'description': 'Enter one feature per line'
        }),
        ('Appearance & Status', {
            'fields': ('color_label', 'is_featured', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    class Media:
        css = {
            'all': ('/admin/css/admin.css',)
        }
