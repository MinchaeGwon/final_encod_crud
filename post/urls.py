from django.urls import path, include
from . import views

urlpatterns = [
    path('post/', views.post_list),
    path('post/<int:pk>/', views.post_detail),
]