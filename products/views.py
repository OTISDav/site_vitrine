from django.shortcuts import render, redirect
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def book_appointment(request):
    return render(request, 'book_appointment.html')
