from django import forms
from django.contrib.auth.models import User
from .models import Facility, Equipment, StaffProfile

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'zone_type', 'description', 'photo', 'capacity', 'features', 'operating_hours']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container',
                'placeholder': 'Facility Name (e.g. Cardio Zone Elite)'
            }),
            'zone_type': forms.Select(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container',
                'rows': 4,
                'placeholder': 'Describe the facility and its purpose...'
            }),
            'capacity': forms.NumberInput(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container'
            }),
            'features': forms.TextInput(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container',
                'placeholder': 'Feature 1, Feature 2, Feature 3...'
            }),
            'operating_hours': forms.TextInput(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container',
                'placeholder': '6:00 AM - 11:00 PM'
            }),
        }

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'category', 'description', 'photo', 'specifications', 'quantity', 'status']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container',
                'placeholder': 'Equipment Name (e.g. Peloton Pro Bike)'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container',
                'rows': 3,
                'placeholder': 'Describe the equipment...'
            }),
            'specifications': forms.TextInput(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container',
                'placeholder': 'Technical specs (e.g. 500W motor, 20 Resistance levels)'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container'
            }),
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container'}),
        }

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['photo', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'w-full bg-surface-container-highest border border-outline-variant/30 rounded-xl px-4 py-3 text-on-surface focus:outline-none focus:ring-1 focus:ring-primary-container', 'rows': 3}),
        }
