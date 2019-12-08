from django.conf.urls import url
from .import views
from django.urls import re_path


app_name = 'user_account'

urlpatterns =[
    re_path(r'^signup/$', views.signup_view, name="signup")
]