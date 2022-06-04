"""Defines URL patterns for vareaze."""

from django.urls import path

from . import views

app_name = 'vareaze'
urlpatterns = [
	# Home page
	path('', views.home, name='home'),
	path('contract/<int:user_id>/', views.initiate, name='initiate'),
]