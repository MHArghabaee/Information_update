from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from accounts.views import login_view
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
