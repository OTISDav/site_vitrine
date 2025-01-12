from django.shortcuts import render, redirect
from .models import Product, ContactMessage
from django.http import HttpResponse
from django.contrib import messages
from .forms import AppointmentForm

def home(request):
    return render(request, 'home.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return HttpResponse("Merci pour votre message !")
    return render(request, 'contact.html')


# from .send_email import send_email  # Assurez-vous d'importer la fonction send_email
from django.conf import settings

def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Sauvegarder le formulaire (réservation)
            appointment = form.save()

            # Détails du rendez-vous
            name = appointment.name
            email = appointment.email
            date = appointment.date
            time = appointment.time

            # Ajouter un message de confirmation à l'utilisateur
            messages.success(request, "Votre rendez-vous a été pris avec succès.")

            # Rediriger vers une page de confirmation ou la même page
            return redirect('book_appointment')  # Changez cela avec le nom correct de l'URL si nécessaire

    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})