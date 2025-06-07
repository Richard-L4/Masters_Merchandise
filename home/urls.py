from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('who-we-are/', views.who_we_are, name='who_we_are'),
]