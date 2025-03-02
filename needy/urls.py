from django.urls import path
from . import views

urlpatterns = [
    path('add_needy/', views.add_needy, name='add_needy'),
]