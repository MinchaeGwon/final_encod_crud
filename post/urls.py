from django.urls import path, include
from . import views

# from rest_framework.routers import DefaultRouter
# from .views import PostViewSet

# router = DefaultRouter()
# router.register('post', PostViewSet)

urlpatterns = [
    path('post/', views.post_list),
    path('post/<int:pk>/', views.post_detail),
    # path('', include(router.urls)), 
]