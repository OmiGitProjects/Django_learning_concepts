from django.urls import path
from .import views

urlpatterns = [
    path('', views.index_, name='homepage'),
    path('date_time/', views.date_time, name='date_time'),
]