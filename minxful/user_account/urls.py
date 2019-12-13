from . import views
from django.urls import path, re_path, include

app_name = "user_account"

urlpatterns = [
    re_path(
        r"^signup/$",
        views.signup_view,
        name="signup"),
    re_path(
        r"^login/$",
        views.login_view,
        name="login"),
    path("logout", views.logout_view, name="logout"),
        ]
