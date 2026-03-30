from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['member', 'check_in', 'check_out', 'zone', 'activity']
    list_filter = ['zone', 'activity']
    search_fields = ['member__first_name', 'member__last_name']
    date_hierarchy = 'check_in'
    readonly_fields = ['created_at']
