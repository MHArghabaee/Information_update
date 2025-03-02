from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_needy, name='add_needy'),
]