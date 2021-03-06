from . import views
from .user_account import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("userdash/", views.userdash),
    re_path(r"^$", views.homepage),
    path("login", views.login),
    path("forum", views.forum),
    path("admindash", views.admindash),
    path("signup", views.signup),
    url(r"^user_account/", include(urls)),
    url(
        r"^logout/$",
        LogoutView.as_view(),
        {"next_page": settings.LOGOUT_REDIRECT_URL},
        name="logout",
    ),
    path("", views.homepage, name="homepage"),
    re_path(
        r"^logout/$",
        LogoutView.as_view(),
        {"next_page": settings.LOGOUT_REDIRECT_URL},
        name="logout",
    ),
]

urlpatterns += staticfiles_urlpatterns()
app_name = "minxful_app"
