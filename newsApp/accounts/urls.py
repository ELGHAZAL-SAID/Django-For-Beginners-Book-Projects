from django.urls import  path
from .views  import  SignUpView,ChangePasswordView, Successful_change_password_view, User_Profile_View, ResetPasswordView,ResetDoneView,ResetConfirmView, ResetCompleteView

urlpatterns = [
    path('signup/',SignUpView.as_view(),name = 'signup'),
    path('password_change/',ChangePasswordView.as_view(),name = 'password_change'),
    path('success/',Successful_change_password_view.as_view(),name = 'success'),
    path('profile/',User_Profile_View.as_view(),name = 'profile'),
    path('password-reset/',ResetPasswordView.as_view(), name = 'password-reset'),
    path('password-reset/done/',ResetDoneView.as_view(),name = 'reset_done'),
    path('password-reset/confirm/',ResetConfirmView.as_view(),name='reset_confirm'),
    path('done/',ResetCompleteView.as_view(),name = 'reset_complete'),
]
