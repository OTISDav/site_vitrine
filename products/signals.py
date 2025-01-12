from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Appointment

@receiver(post_save, sender=Appointment)
def send_appointment_notification(sender, instance, created, **kwargs):
    if created:
        # Un nouveau rendez-vous a été créé
        subject = "Nouveau rendez-vous pris"
        message = f"""
        Un nouveau rendez-vous a été pris :
        Nom : {instance.name}
        Email : {instance.email}
        Date : {instance.date}
        Heure : {instance.time}
        """
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False
            )
            print("Email de notification envoyé.")
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email : {e}")
