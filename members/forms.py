from django import forms
from django.contrib.auth.models import User
from .models import Member


class MemberForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full focus:ring-primary focus:border-primary',
            'placeholder': 'Desired username'
        })
    )
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full focus:ring-primary focus:border-primary',
            'placeholder': '••••••••'
        })
    )
    confirm_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full focus:ring-primary focus:border-primary',
            'placeholder': '••••••••'
        })
    )

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['username'].initial = self.instance.user.username
        
        # If adding new, password is required
        if not self.instance.pk:
            self.fields['password'].required = True
            self.fields['confirm_password'].required = True

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            qs = User.objects.filter(username=username)
            if self.instance and self.instance.user:
                qs = qs.exclude(pk=self.instance.user.pk)
            if qs.exists():
                raise forms.ValidationError("This username is already taken.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password or confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        member = super().save(commit=False)
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not member.user:
            # Create new user
            user = User.objects.create_user(
                username=username,
                email=member.email,
                password=password,
                first_name=member.first_name,
                last_name=member.last_name
            )
            member.user = user
        else:
            # Update existing user
            user = member.user
            user.username = username
            user.email = member.email
            user.first_name = member.first_name
            user.last_name = member.last_name
            if password:
                user.set_password(password)
            user.save()

        if commit:
            member.save()
        return member


def from_plans_import():
    from plans.models import MembershipPlan
    return MembershipPlan.objects.all()


class MemberSignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
            'placeholder': 'Last Name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
            'placeholder': 'email@example.com'
        })
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
            'placeholder': 'Phone Number'
        })
    )
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
            'placeholder': 'Choose a username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
            'placeholder': 'Minimum 8 characters'
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full',
            'placeholder': 'Repeat password'
        })
    )
    plan = forms.ModelChoiceField(
        queryset=from_plans_import(),
        widget=forms.Select(attrs={
            'class': 'form-select bg-surface-container-highest border-outline-variant text-on-surface rounded-xl px-4 py-3 w-full'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from plans.models import MembershipPlan
        self.fields['plan'].queryset = MembershipPlan.objects.filter(is_active=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Member.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
