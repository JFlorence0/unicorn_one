"""Defines URL patterns for vareaze."""

from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
	# Home page
	path('register/', views.register, name='register'),
	path('logout/', views.logged_out, name='logged_out'),
	path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
]