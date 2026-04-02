from django import forms
from .models import GymClass

class GymClassForm(forms.ModelForm):
    class Meta:
        model = GymClass
        fields = [
            'name', 'instructor', 'description', 'day', 
            'start_time', 'duration_minutes', 'capacity', 
            'difficulty', 'icon', 'color_label', 'photo'
        ]
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full bg-surface-container-highest border-outline-variant/20 rounded-xl text-on-surface focus:ring-primary-container'}),
            'description': forms.Textarea(attrs={'rows':3, 'class': 'w-full bg-surface-container-highest border-outline-variant/20 rounded-xl text-on-surface focus:ring-primary-container'}),
            'name': forms.TextInput(attrs={'class': 'w-full bg-surface-container-highest border-outline-variant/20 rounded-xl text-on-surface focus:ring-primary-container'}),
            'instructor': forms.TextInput(attrs={'class': 'w-full bg-surface-container-highest border-outline-variant/20 rounded-xl text-on-surface focus:ring-primary-container'}),
            'day': forms.Select(attrs={'class': 'w-full bg-surface-container-highest border-outline-variant/20 rounded-xl text-on-surface focus:ring-primary-container'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'w-full bg-surface-container-highest border-outline-variant/20 rounded-xl text-on-surface focus:ring-primary-container'}),
            'capacity': forms.NumberInput(attrs={'class': 'w-full bg-surface-container-highest border-outline-variant/20 rounded-xl text-on-surface focus:ring-primary-container'}),
            'difficulty': forms.Select(attrs={'class': 'w-full bg-surface-container-highest border-outline-variant/20 rounded-xl text-on-surface focus:ring-primary-container'}),
            'icon': forms.TextInput(attrs={'class': 'w-full bg-surface-container-highest border-outline-variant/20 rounded-xl text-on-surface focus:ring-primary-container', 'placeholder': 'e.g., fitness_center'}),
            'color_label': forms.Select(choices=[('primary', 'Primary (Neon)'), ('secondary', 'Secondary (Cyan)'), ('tertiary', 'Tertiary (Gold)')], attrs={'class': 'w-full bg-surface-container-highest border-outline-variant/20 rounded-xl text-on-surface focus:ring-primary-container'}),
            'photo': forms.FileInput(attrs={'class': 'w-full bg-surface-container-highest border-outline-variant/20 rounded-xl text-on-surface focus:ring-primary-container'}),
        }
