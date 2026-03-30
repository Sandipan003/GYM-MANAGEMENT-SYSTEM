from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['member_id', 'first_name', 'last_name', 'email', 'plan', 'status', 'join_date']
    list_filter = ['status', 'plan']
    search_fields = ['first_name', 'last_name', 'email', 'member_id']
    readonly_fields = ['member_id', 'created_at', 'updated_at']
    ordering = ['-created_at']
