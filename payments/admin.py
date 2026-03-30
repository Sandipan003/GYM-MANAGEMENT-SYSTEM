from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['member', 'plan', 'amount', 'payment_date', 'payment_method', 'status']
    list_filter = ['status', 'payment_method']
    search_fields = ['member__first_name', 'member__last_name', 'transaction_id']
    date_hierarchy = 'payment_date'
