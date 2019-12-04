from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path(r'^(?P<slug>[\w-]+)/$', views.post_detail),


]
