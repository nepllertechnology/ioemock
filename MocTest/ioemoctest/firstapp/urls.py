from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index),
<<<<<<< HEAD
    path('start_test/<str:subject_id>/', views.start_test, name='start_test'),
    path('submit_test/', views.submit_test, name='submit_test'),
=======
    path('question/', views.question_page, name='question_page'),
>>>>>>> refs/remotes/origin/qnsdisplay
]
