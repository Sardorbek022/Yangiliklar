from  django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

# from .views import (
#     UserLogin, 
# )


urlpatterns = [
    # path('login/', view=UserLogin.as_view(), name='login_page'),
    path('login/', view=LoginView.as_view(), name='login_page'),
    path('logout/', view=LogoutView.as_view(), name='logout_page'),
]