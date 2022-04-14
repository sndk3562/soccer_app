
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('soccer.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),


]

urlpatterns += staticfiles_urlpatterns()

