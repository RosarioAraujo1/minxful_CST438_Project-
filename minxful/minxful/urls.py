from django.contrib import admin
from django.urls import path, include
from minxful_app import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userdash/', views.userdash),
    path("", views.homepage),
    path('login', views.login),
    path('forum', views.forum),
    path('admindash', views.admindash),
    path('signup', views.signup),
    url(r'^user_account/', include('user_account.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root':settings.MEDIA_ROOT,
        }),
    ]
