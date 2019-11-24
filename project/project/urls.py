
from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userdash/', views.userdash),
    path("", views.homepage),
    path('login', views.login),
    path('forum', views.forum),
    path('admindash', views.admindash),
    path('signup',views.signup),
]
