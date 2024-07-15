from  django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)

from .views import (
    UserLogin, DashboardView 
)


urlpatterns = [
    # path('login/', view=UserLogin.as_view(), name='login_page'),
    path('login/', view=LoginView.as_view(), name='login_page'),
    path('logout/', view=LogoutView.as_view(), name='logout_page'),
    path('password-change/', view=PasswordChangeView.as_view(), name='password-change_page'),
    path('password-change-done/', view=PasswordChangeDoneView.as_view(), name='password_change_done_page'),
    path('profile/', view=DashboardView.as_view(), name='user_profile_page'),
]