from django.shortcuts import render, redirect
from .models import Product, ContactMessage
from django.http import HttpResponse
from django.contrib import messages
from .forms import AppointmentForm

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


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

from django.conf import settings
from twilio.rest import Client
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm

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

            # Notification WhatsApp à l'administrateur
            try:
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                message_body = f"""
                Nouvelle réservation de rendez-vous :
                Nom : {name}
                Email : {email}
                Date : {date}
                Heure : {time}
                """
                client.messages.create(
                    from_=settings.TWILIO_WHATSAPP_NUMBER,
                    to=settings.ADMIN_WHATSAPP_NUMBER,
                    body=message_body
                )
                print("Notification WhatsApp envoyée à l'administrateur.")
            except Exception as e:
                print(f"Erreur lors de l'envoi de la notification WhatsApp : {e}")

            # Ajouter un message de confirmation à l'utilisateur
            messages.success(request, "Votre rendez-vous a été pris avec succès.")

            # Rediriger vers une page de confirmation ou la même page
            return redirect('book_appointment')  # Changez cela avec le nom correct de l'URL si nécessaire

    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})
