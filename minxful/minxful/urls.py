from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from minxful_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userdash/', views.userdash),
    path("", views.homepage),
    path('login', views.login),
    path('forum', views.forum),
    path('admindash', views.admindash),
    path('signup', views.signup),
    re_path(r'^accounts/', include('accounts.urls')),
]


urlpatterns += staticfiles_urlpatterns()
