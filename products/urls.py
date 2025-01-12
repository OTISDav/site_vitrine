from django.urls import path
from . import views
from .views import book_appointment


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('rendezvous/', book_appointment, name='book_appointment'),
]
