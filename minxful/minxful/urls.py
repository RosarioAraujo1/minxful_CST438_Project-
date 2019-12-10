from django.contrib import admin
from django.urls import path, include, re_path
from minxful_app import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("userdash/", views.userdash),
    re_path(r"^$", views.homepage),
    path("login", views.login),
    path("forum", views.forum),
    path("admindash", views.admindash),
    path("signup", views.signup),
    url(r"^user_account/", include("user_account.urls")),
    url(
        r"^logout/$",
        LogoutView.as_view(),
        {"next_page": settings.LOGOUT_REDIRECT_URL},
        name="logout",
    ),
]


urlpatterns += staticfiles_urlpatterns()
