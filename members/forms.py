from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'photo', 'plan', 'status', 'join_date',
            'membership_expiry', 'address', 'emergency_contact', 'notes'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full focus:ring-primary focus:border-primary',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'placeholder': 'email@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'placeholder': '+91 9999999999'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'accept': 'image/*'
            }),
            'plan': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'join_date': forms.DateInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'type': 'date'
            }),
            'membership_expiry': forms.DateInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'type': 'date'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-textarea bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'rows': 3,
                'placeholder': 'Full address...'
            }),
            'emergency_contact': forms.TextInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'placeholder': 'Name & Phone Number'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-textarea bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'rows': 3,
                'placeholder': 'Additional notes...'
            }),
        }
