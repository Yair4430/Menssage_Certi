import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(destinatario, asunto, cuerpo, remitente, clave_app):
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.attach(MIMEText(cuerpo, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(remitente, clave_app)
            servidor.sendmail(remitente, destinatario, msg.as_string())
        print(f"📧 Correo enviado a {destinatario}")
    except Exception as e:
        print(f"❌ Error enviando correo a {destinatario}: {e}")

