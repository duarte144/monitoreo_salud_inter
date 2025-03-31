from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from .views import custom_logout


urlpatterns = [
    path('', views.index, name='index'),
    path('agregar-gato/', views.agregar_gato, name='agregar_gato'),
    path('editar-gato/<int:gato_id>/', views.editar_gato, name='editar_gato'),
    path('eliminar-gato/<int:gato_id>/', views.eliminar_gato, name='eliminar_gato'),
    path('agregar-registro/', views.agregar_registro, name='agregar_registro'),
    path('editar-registro/<int:registro_id>/', views.editar_registro, name='editar_registro'),
    path('eliminar-registro/<int:registro_id>/', views.eliminar_registro, name='eliminar_registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('logout-success/', lambda request: render(request, 'appmonitoreo/logout_success.html'), name='logout_success'),
    path("logout/", custom_logout, name="logout"),
    
]
