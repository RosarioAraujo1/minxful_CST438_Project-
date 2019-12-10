from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView
from django.conf import settings

app_name = "minxful_app"
urlpatterns = [
        path('', views.homepage, name='homepage'),
        re_path(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
urlpatterns += staticfiles_urlpatterns()
