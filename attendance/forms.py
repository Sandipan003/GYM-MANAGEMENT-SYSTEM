from django import forms
from .models import Attendance
from members.models import Member


class AttendanceCheckInForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['member', 'zone', 'activity', 'notes']
        widgets = {
            'member': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'zone': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'activity': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-textarea bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'rows': 2
            }),
        }


class AttendanceEditForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['member', 'check_in', 'check_out', 'zone', 'activity', 'notes']
        widgets = {
            'member': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'check_in': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'check_out': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'zone': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'activity': forms.Select(attrs={
                'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-textarea bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
                'rows': 2
            }),
        }
