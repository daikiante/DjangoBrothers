from django.urls import path
from . import views

from  django.contrib.auth import views as auth_view
urlpatterns = [
    path('register/', views.register, name='register'),
  # Login
	path('login/', auth_view.LoginView.as_view(), name='login'),
	# Logout
	path('logout/', auth_view.LogoutView.as_view(), name='logout'),


]
