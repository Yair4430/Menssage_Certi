from twilio.rest import Client

def enviar_whatsapp(mensaje, telefono, sid, token, remitente_whatsapp):
    try:
        client = Client(sid, token)
        message = client.messages.create(
            from_='whatsapp:' + remitente_whatsapp,
            body=mensaje,
            to='whatsapp:' + str(telefono)
        )
        print(f"📲 WhatsApp enviado a {telefono}")
    except Exception as e:
        print(f"❌ Error enviando WhatsApp a {telefono}: {e}")

