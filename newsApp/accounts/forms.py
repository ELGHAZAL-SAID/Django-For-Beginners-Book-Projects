from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email','age',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','email','age',)

class CustomUserChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ('password',)  # Use a tuple to specify fields

class CustomUserPasswordResetForm(PasswordResetForm):
    class Meta:
        fields = ('email',) # Use a tuple to specify fields

class CustomPasswordResetConfirmForm(SetPasswordForm):
    
    class Meta:
        fields = ('password',) # Use a tuple to specify fields