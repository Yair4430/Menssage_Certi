from plantilla_utils import crear_plantilla_excel
from correo_utils import enviar_correo
from whatsapp_utils import enviar_whatsapp
from excel_utils import cargar_datos_excel, personalizar_mensaje

def cargar_plantilla_mensaje(ruta='plantilla_mensaje.txt'):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return archivo.read()

# main.py
def enviar_mensajes_correo(remitente, clave, ruta_excel):
    datos = cargar_datos_excel(ruta_excel)
    plantilla = cargar_plantilla_mensaje()

    for _, fila in datos.iterrows():
        mensaje = personalizar_mensaje(plantilla, fila.to_dict())
        asunto = "Inconsistencias en Documentación - Proceso de Certificación"
        enviar_correo(fila['Correo'], asunto, mensaje, remitente, clave)

def enviar_mensajes_whatsapp(sid, token, remitente_whatsapp, ruta_excel):
    datos = cargar_datos_excel(ruta_excel)
    plantilla = cargar_plantilla_mensaje()

    for _, fila in datos.iterrows():
        mensaje = personalizar_mensaje(plantilla, fila.to_dict())
        enviar_whatsapp(mensaje, fila['Telefono'], sid, token, remitente_whatsapp)
