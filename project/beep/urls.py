from django.urls import path
from . import views

urlpatterns= [
    path('', views.selection, name='select'),
    path('home/', views.home, name= 'home')
]