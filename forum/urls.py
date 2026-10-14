from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('fale-conosco/', views.fale_conosco, name='fale_conosco'),
]