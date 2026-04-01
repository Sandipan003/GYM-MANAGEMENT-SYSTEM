from django.contrib import admin
from .models import Equipment, Facility


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'status')
    list_filter = ('category', 'status')
    search_fields = ('name', 'description')
    fieldsets = (
        ('Basic Info', {'fields': ('name', 'category', 'description')}),
        ('Details', {'fields': ('photo', 'specifications', 'quantity', 'status')}),
    )


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'zone_type', 'capacity')
    list_filter = ('zone_type',)
    search_fields = ('name', 'description')
    fieldsets = (
        ('Basic Info', {'fields': ('name', 'zone_type', 'description')}),
        ('Details', {'fields': ('photo', 'capacity', 'features', 'operating_hours')}),
    )
