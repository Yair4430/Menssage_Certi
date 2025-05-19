import pandas as pd

def cargar_datos_excel(ruta_archivo):
    try:
        df = pd.read_excel(ruta_archivo)
        return df
    except Exception as e:
        print(f"❌ Error cargando Excel: {e}")
        return None

def personalizar_mensaje(plantilla, datos):
    return plantilla.format(**datos)
import pandas as pd

def cargar_datos_excel(ruta_excel):
    try:
        return pd.read_excel(ruta_excel)
    except Exception as e:
        print(f"❌ Error cargando Excel: {e}")
        return None

def personalizar_mensaje(plantilla, datos):
    for clave, valor in datos.items():
        plantilla = plantilla.replace(f'{{{clave}}}', str(valor))
    return plantilla
