from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toys/new/', views.toy_create, name='create_toy'),
    path('toys/<int:pk>/', views.toy, name='toy'),
    path('about/', views.about, name='about')
]
