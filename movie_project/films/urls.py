from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='page1'),
    path('add/', views.add, name='page2'),
]