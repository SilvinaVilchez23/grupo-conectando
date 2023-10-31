import tkinter as tk
from tkinter import messagebox
import cifrado_atbash as cifrar_atbash
import cifrado_cesar as cifrar_cesar

def abrir_ventana_principal():
    ventana_welcome.destroy()
    ventana_principal = tk.Tk()
    ventana_principal.title("TP Grupal Parte 1 - Grupo: Conectando")
    ventana_principal.geometry("500x400")
    ventana_principal.iconbitmap("elicono.ico")

    def procesar_mensaje():
        mensaje = entrada_mensaje.get()
        metodo = metodo_seleccionado.get()
        clave = entrada_clave.get()

        if metodo == "César":
            clave = str(clave)
            if accion_seleccionada.get() == "Cifrar":
                mensaje_procesado = cifrar_cesar(mensaje, clave)
            else:
                mensaje_procesado = cifrar_cesar(mensaje, -clave)  # Descifrado con clave -N
        else:
            mensaje_procesado = cifrar_atbash.Cifrado_Atbash(mensaje)  # Cifrado o descifrado con Atbash

        resultado.config(text="Resultado: " + mensaje_procesado)

    metodo_seleccionado = tk.StringVar()
    entrada_mensaje = tk.Entry(ventana_principal, width=40)
    entrada_clave = tk.Entry(ventana_principal, width=40)
    
    metodo_frame = tk.Frame(ventana_principal)
    metodo_frame.pack()

    tk.Label(metodo_frame, text="Seleccione el método:").pack()
    tk.Radiobutton(metodo_frame, text="César", variable=metodo_seleccionado, value="César").pack()
    tk.Radiobutton(metodo_frame, text="Atbash", variable=metodo_seleccionado, value="Atbash").pack()

    accion_seleccionada = tk.StringVar()
    tk.Label(ventana_principal, text="Ingrese el mensaje:").pack()
    entrada_mensaje.pack()
    tk.Label(ventana_principal, text="Ingrese la clave (solo para César):").pack()
    entrada_clave.pack()
    tk.Radiobutton(ventana_principal, text="Cifrar", variable=accion_seleccionada, value="Cifrar").pack()
    tk.Radiobutton(ventana_principal, text="Descifrar", variable=accion_seleccionada, value="Descifrar").pack()

    tk.Button(ventana_principal, text="Procesar Mensaje", command=procesar_mensaje).pack()
    resultado = tk.Label(ventana_principal, text="Resultado: ", font=(None, 12))
    resultado.pack()

    ventana_principal.mainloop()

# Resto del código como antes

# Ventana de bienvenida
ventana_welcome = tk.Tk()
ventana_welcome.title("TP Grupal Parte 1 - Grupo Conectando")
ventana_welcome.geometry("500x400")
ventana_welcome.iconbitmap("elicono.ico")
mensaje_bienvenida = "Bienvenido a la aplicación de mensajes secretos del grupo Conectando.\n"\
                     "Para continuar, presione continuar, de lo contrario cierre la ventana"

etiqueta_bienvenida = tk.Label(ventana_welcome, text=mensaje_bienvenida, font=20)
etiqueta_bienvenida.pack()

boton_continuar = tk.Button(ventana_welcome, text="Continuar", font=30, command=abrir_ventana_principal)
boton_continuar.pack()

etiqueta_construido = tk.Label(ventana_welcome, text="Construída por:", font=20)
etiqueta_construido.pack()

# Lista de nombres de miembros del grupo
miembros_grupo = ["SILVINA VILCHEZ", "MARIA FERRARA", "BRIAN MAMANI", "NAHUEL CABRERA"]
for miembro in miembros_grupo:
    etiqueta_miembro = tk.Label(ventana_welcome, text=miembro, font=25)
    etiqueta_miembro.pack()

ventana_welcome.mainloop()
