from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('needy.urls'), name='needy'),
    path('', include('accounts.urls'), name='accounts'),

]
