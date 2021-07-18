from django.contrib.auth.views import LoginView, LogoutView


class UserLoginView(LoginView):
    template_name = 'userauth/login.html'


class UserLogoutView(LogoutView):
    template_name = 'userauth/logout.html'

