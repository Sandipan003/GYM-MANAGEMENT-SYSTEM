from django import forms
from .models import MembershipPlan


class PlanForm(forms.ModelForm):
    class Meta:
        model = MembershipPlan
        fields = ['name', 'slug', 'price', 'duration_months', 'description', 'features', 'is_featured', 'color_label', 'photo', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'placeholder': 'e.g. Elite Performance'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'placeholder': 'e.g. elite-performance'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'placeholder': '0.00', 'step': '0.01'
            }),
            'duration_months': forms.NumberInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'min': '1'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'rows': 2
            }),
            'features': forms.Textarea(attrs={
                'class': 'form-textarea bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'rows': 6,
                'placeholder': 'One feature per line:\n24/7 Access\nPersonal Training\nSpa Access'
            }),
            'color_label': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-checkbox rounded text-primary-container'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-checkbox rounded text-primary-container'
            }),
        }
