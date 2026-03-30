from django import forms
from .models import Payment
from members.models import Member


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['member', 'plan', 'amount', 'payment_date', 'payment_method', 'status', 'transaction_id', 'notes']
        widgets = {
            'member': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'plan': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'step': '0.01'
            }),
            'payment_date': forms.DateInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'type': 'date'
            }),
            'payment_method': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'transaction_id': forms.TextInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'placeholder': 'TXN-XXXXXXXX'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-textarea bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'rows': 3
            }),
        }
