from django.urls import path 
from . import views

urlpatterns = [path('get-tickets/', views.get_tickets, name='get_tickets'), path('generate-pdf', views.generate_pdf, name='generate_pdf'),] #add more url paths as needed]

