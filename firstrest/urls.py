
from django.contrib import admin
from django.urls import path, include
import post.urls
from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path("rest-auth/", include('rest_auth.urls')),
    path('rest-auth/registration', include('rest_auth.registration.urls')),
]
 

