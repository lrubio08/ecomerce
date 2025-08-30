import smtplib
import ssl
from django.core.mail import EmailMessage
from django.conf import settings
from email.mime.text import MIMEText

from email.mime.text import MIMEText
import smtplib
from django.conf import settings

def enviar_correo(subject, body, recipient_list, is_html=False):
    try:
        # Configura el contenido HTML con MIMEText
        if is_html:
            message = MIMEText(body, "html", "utf-8")
        else:
            message = MIMEText(body, "plain", "utf-8")

        # Configura las cabeceras del correo
        message["Subject"] = subject
        message["From"] = settings.DEFAULT_FROM_EMAIL
        message["To"] = ", ".join(recipient_list)

        # Envía el correo con SMTP
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.starttls()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(settings.DEFAULT_FROM_EMAIL, recipient_list, message.as_string())
        server.quit()

        print(f"Correo enviado correctamente a {recipient_list}")
    except Exception as e:
        print(f"Error enviando correo: {e}")



