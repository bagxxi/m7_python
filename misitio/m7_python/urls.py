from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView, name='home'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', LoginView.as_view(next_page='dashboard'), name='login'),
    path('register/', views.registerView, name='register'),
    path('register_tipo/', views.register_tipoView, name='register_tipo_url'),
    path('new_inmueble/', views.new_inmuebleView, name='new_inmueble_url'),
    path('udpate_profile/', views.profile, name='update_profile'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]