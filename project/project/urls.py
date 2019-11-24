
from django.contrib import admin
from django.urls import path
from .import views
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path("", views.homepage),
]
