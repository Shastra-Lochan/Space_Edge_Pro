from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.default, name = 'Default'),
    path('home', views.index, name = 'Home'),
    path('about',views.about, name = "about"),
    path('founders', views.founders, name = "founders"),
    path('contact', views.contact, name = "contact"),
]
