from re import template
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangePasswordForm, CustomUserPasswordResetForm, PasswordResetForm,CustomPasswordResetConfirmForm

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name =  'registration/signup.html'

class ChangePasswordView(PasswordChangeView):
    form_class = CustomUserChangePasswordForm
    success_url = reverse_lazy('success')
    template_name = 'registration/changePassword.html'

class Successful_change_password_view(PasswordChangeView):
    form_class = CustomUserChangePasswordForm
    success_url = reverse_lazy('login')
    template_name = 'registration/password_change_done.html'

class ResetPasswordView(PasswordResetView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('reset_done')
    template_name = 'registration/reset_password.html'

class ResetDoneView(TemplateView):
    template_name = 'registration/reset_done.html'

class ResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    template_name = 'registration/reset_confirm.html'
    success_url = reverse_lazy('reset_complete')

class ResetCompleteView(TemplateView):
    template_name = 'registration/reset_complete.html'

class User_Profile_View(TemplateView):
    template_name = 'registration/profile.html'