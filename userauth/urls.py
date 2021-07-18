from django.urls import path
from userauth.views import UserLoginView, UserLogoutView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
