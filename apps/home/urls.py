from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.PruevaVIEW.as_view()),
    path('prueba/listview', views.PruebaListView.as_view()),
    path('lista-prueba', views.ListarPruebasView.as_view()),
    path('add/', views.PruebaCreateView.as_view()),
]
