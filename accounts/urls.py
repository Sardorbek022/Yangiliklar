from  django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
)

from .views import (
    UserLogin, DashboardView, UserRegistrationView, 
    # SignUpView, 
    Edit_User_View, EditUserView
    
)


urlpatterns = [
    path('register/', view=UserRegistrationView, name='register_page'),
    # path('signup/', view=SignUpView.as_view(), name='register_page'),
    # path('login/', view=UserLogin.as_view(), name='login_page'),
    path('login/', view=LoginView.as_view(), name='login_page'),
    path('logout/', view=LogoutView.as_view(), name='logout_page'),
    path('password-change/', view=PasswordChangeView.as_view(), name='password-change_page'),
    path('password-change-done/', view=PasswordChangeDoneView.as_view(), name='password_change_done_page'),
    path('password-reset/', 
     PasswordResetView.as_view(
        html_email_template_name='registration/password_reset_email.html'
    ),
    name='password-reset'
),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    path('profile/', view=DashboardView.as_view(), name='user_profile_page'),
    path('user-edit/', view=Edit_User_View, name='user_edit_page'),
    # path('user-edit/', view=EditUserView.as_view(), name='user_edit_page'),
]