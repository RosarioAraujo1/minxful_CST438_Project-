from django.urls import include, re_path
from django.contrib import admin
from django.urls import path
from minxful_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userdash/', views.userdash),
    path("", views.homepage),
    path('login', views.login),
    re_path(r'^about/$', views.forum),
    path('admindash', views.admindash),
    path('signup',views.signup),
]


urlpatterns += staticfiles_urlpatterns()