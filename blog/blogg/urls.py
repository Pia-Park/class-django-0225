from django.urls import path
from . import views

app_name = 'blogg'

urlpatterns= [
    path('', views.home, name='homepage')
]