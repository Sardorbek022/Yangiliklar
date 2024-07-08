from  django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    UserLogin, DashboardView 
)


urlpatterns = [
    # path('login/', view=UserLogin.as_view(), name='login_page'),
    path('login/', view=LoginView.as_view(), name='login_page'),
    path('logout/', view=LogoutView.as_view(), name='logout_page'),
    path('profile/', view=DashboardView.as_view(), name='user_profile_page'),
]