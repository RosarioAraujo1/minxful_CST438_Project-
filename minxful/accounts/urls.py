from django.contrib.urls import url
from .import views
from django.urls import include, re_path

app_name ='accounts'

urlpatterns = [
    re_path(r'^signup/$'. views.signup_view, name="signup")

]