from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_view,name='login'), 
    path('logout',views.logout_view,name='logout'),
    path('Register',views.registration,name='register'),
    path('Admin',views.admin_login_view,name='Admin'),
    path('dashboard',views.dashboard_view,name='dashboard'),
    path('udashboard',views.udashboard_view,name='udashboard'),
    path('adopt/<int:pk>',views.pet_adopt,name='Adopt'),
]