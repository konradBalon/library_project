from django.contrib import admin
from django.urls import path
from library import views
urlpatterns = [
    path('', views.landing_page),
]
