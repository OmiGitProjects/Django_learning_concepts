from django.urls import path
from .import views

urlpatterns = [
    path('', views.showform_data, name='register'),
]
