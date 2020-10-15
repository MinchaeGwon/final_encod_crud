
from django.contrib import admin
from django.urls import path, include
import post.urls
from rest_framework import urls
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('post.urls')),
    path('', include('post.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path("rest-auth/", include('rest_auth.urls')),
    path('rest-auth/registration', include('rest_auth.registration.urls')),
    path('api/token/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
]
 

