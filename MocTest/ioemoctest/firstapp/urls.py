from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index),
    path('start_test/<str:subject_id>/', views.start_test, name='start_test'),
    path('submit_test/', views.submit_test, name='submit_test'),
]
