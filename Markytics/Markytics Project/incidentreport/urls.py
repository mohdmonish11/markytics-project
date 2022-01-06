
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name='forms'),
    path('check_form_inputs',views.check_form_inputs, name='formCheck'),
    path('completeField/', views.completeField),
    path('successfull_login/', views.successfull_login),
]
