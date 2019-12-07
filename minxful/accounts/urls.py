from django.conf.urls import url
from .import views
from django.urls import include, path, re_path


app_name = 'accounts'


urlpatterns =[
    re_path(r'^signup/$', views.signup_view, name="signup")
]