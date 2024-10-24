from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserEmailForm(forms.Form):
    email =forms.EmailField()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'skill_profile', 'total_completed_task']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

