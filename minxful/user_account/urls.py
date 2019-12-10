from . import views
from django.urls import re_path, include

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
    re_path(
        r"^",
        include(
            "minxful_app.urls",
            namespace="minxful_app")),
app_name = 'user_account'

urlpatterns = [
    re_path(r'^signup/$', views.signup_view, name="signup"),
    re_path(r'^login/$', views.login_view, name="login"),
    re_path(r'^logout/$', views.logout_view, name="logout"),
]
