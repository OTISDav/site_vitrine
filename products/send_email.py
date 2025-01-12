# import sendgrid
# from sendgrid.helpers.mail import Mail, Email, To, Content
# from django.conf import settings
#
#
# def send_email(to_email, subject, content):
#     sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
#     from_email = Email(settings.DEFAULT_FROM_EMAIL)  # L'email de l'expéditeur
#     to_email = To(to_email)  # L'email du destinataire
#     content = Content("text/plain", content)  # Le contenu de l'email
#
#     mail = Mail(from_email, to_email, subject, content)
#
#     try:
#         response = sg.send(mail)
#         return response
#     except Exception as e:
#         print(f"Erreur lors de l'envoi de l'email : {e}")
#         return None
