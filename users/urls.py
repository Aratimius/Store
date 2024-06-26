from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    RegisterView,
    ProfileView,
    generate_password,
    activate_user,
    congratulations,
)

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/genpassword/", generate_password, name="generate_password"),
    path("activate/<uuid:uid>", activate_user, name="activate_user"),
    path("congratulations/", congratulations, name="congratulations"),
]
