from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_needy, name='add_needy'),
    path('success/', views.success_view, name='success_view'),
    path('list/', views.needy_list, name='needy_list'),
    path('needy/delete/<int:id>/', views.delete_needy, name='delete_needy'),
    path('export_needy/', views.export_needy_to_excel, name='export_needy_to_excel'),
]
