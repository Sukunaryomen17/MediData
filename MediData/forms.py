from django import forms
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(forms.ModelForm):
    # Custom fields not in the default User model
    full_name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date of Birth")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'dob', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data
