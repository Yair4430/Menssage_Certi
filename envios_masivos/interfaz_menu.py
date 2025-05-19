import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from main import crear_plantilla_excel, enviar_mensajes_correo, enviar_mensajes_whatsapp

def crear_plantilla():
    crear_plantilla_excel()
    messagebox.showinfo("Éxito", "✅ Plantilla Excel creada correctamente.")

def enviar_correos():
    ruta_excel = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Archivos Excel", "*.xlsx")])
    if not ruta_excel:
        messagebox.showwarning("Advertencia", "⚠️ No se seleccionó un archivo.")
        return

    remitente = simpledialog.askstring("Correo", "Ingrese el correo Gmail del remitente:")
    clave = simpledialog.askstring("Contraseña", "Ingrese la contraseña de aplicación de Gmail:", show='*')

    if remitente and clave:
        try:
            enviar_mensajes_correo(remitente, clave, ruta_excel)
            messagebox.showinfo("Éxito", "📧 Correos enviados correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Ocurrió un error:\n{e}")
    else:
        messagebox.showwarning("Advertencia", "⚠️ Debe ingresar todos los datos.")

def enviar_whatsapp():
    ruta_excel = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Archivos Excel", "*.xlsx")])
    if not ruta_excel:
        messagebox.showwarning("Advertencia", "⚠️ No se seleccionó un archivo.")
        return

    sid = simpledialog.askstring("SID", "Ingrese el Twilio SID:")
    token = simpledialog.askstring("Token", "Ingrese el Twilio Auth Token:", show='*')
    remitente = simpledialog.askstring("Remitente", "Ingrese el número de WhatsApp Twilio (ej: +14155238886):")

    if sid and token and remitente:
        try:
            enviar_mensajes_whatsapp(sid, token, remitente, ruta_excel)
            messagebox.showinfo("Éxito", "💬 Mensajes de WhatsApp enviados correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Ocurrió un error:\n{e}")
    else:
        messagebox.showwarning("Advertencia", "⚠️ Debe ingresar todos los datos.")

def lanzar_interfaz():
    ventana = tk.Tk()
    ventana.title("Envío de Mensajes")
    ventana.geometry("300x280")
    ventana.configure(bg="#f0f0f0")

    tk.Label(ventana, text="📤 ENVÍO DE MENSAJES", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=20)

    tk.Button(ventana, text="📄 Crear Plantilla Excel", width=30, command=crear_plantilla).pack(pady=5)
    tk.Button(ventana, text="✉️ Enviar Correos", width=30, command=enviar_correos).pack(pady=5)
    tk.Button(ventana, text="💬 Enviar WhatsApp", width=30, command=enviar_whatsapp).pack(pady=5)
    tk.Button(ventana, text="❌ Salir", width=30, command=ventana.destroy).pack(pady=20)

    ventana.mainloop()

if __name__ == "__main__":
    lanzar_interfaz()
