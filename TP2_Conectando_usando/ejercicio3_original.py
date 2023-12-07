from tkinter import *
import Cifrado_Atbash as cifrar_atbash
import cifrado_cesar as cifrar_cesar
import cifrado_cesar as descifrar_cesar

def main() :
    
    ventana_welcome = Tk()
    ventana_welcome.config(bg="purple")
    ventana_welcome.iconbitmap(r"icono.ico")
    ventana_welcome.title("TP Grupal Parte 1 - Grupo Conectando")

    mensaje_bienvenida = "Bienvenido a la aplicación de mensajes secretos del grupo Conectando.\n"\
                    "Para continuar, presione continuar, de lo contrario cierre la ventana"

    etiqueta_bienvenida = Label(ventana_welcome, text=mensaje_bienvenida)
    etiqueta_bienvenida.pack()

    boton_continuar = Button(ventana_welcome, text="Continuar", command=lambda:abrir_ventana_principal(ventana_welcome))
    boton_continuar.pack()
    info_grupo = Label(ventana_welcome, text="Construída por : SILVINA VILCHEZ, MARIA FERRARA, BRIAN MAMANI, NAHUEL CABRERA")
    info_grupo.pack()

    ventana_welcome.mainloop()
    
def abrir_ventana_principal(main):
    main.destroy()
    ventana_principal = Tk()
    ventana_principal.config(bg="pink")
    
    ventana_principal.iconbitmap(r"icono.ico")    
    ventana_principal.title("TP Grupal Parte 1 - Grupo: Conectando")
    
    def procesar_mensaje():
        mensaje = ingresar_mensaje.get()
        metodo = metodo_seleccionado.get()
        clave = ingresar_clave.get()

        if metodo == "César":
            clave = int(clave)          
            if accion_seleccionada.get() == "Cifrar":
                mensaje_procesado = cifrar_cesar.codigo_cesar(mensaje, clave)
                resultado.config(text="Resultado: " + mensaje_procesado) 
            else:
                mensaje_procesado = descifrar_cesar.codigo_cesar(mensaje, -clave)  # Descifrado con clave -N
                resultado.config(text="Resultado: " + mensaje_procesado)

        else:
            mensaje_procesado = cifrar_atbash.Cifrado_Atbash(mensaje)  # Cifrado o descifrado con Atbash

        resultado.config(text="Resultado: " + mensaje_procesado)
    
    metodo_seleccionado = StringVar()
        
    ingresar_mensaje = Entry(ventana_principal, width=40)
    ingresar_clave = Entry(ventana_principal, width=40)
    
    Miframe = Frame(ventana_principal)
    Miframe.pack()
    
    seleccion = Label(Miframe, text="Seleccione el método:")
    seleccion.pack()

    accion_seleccionada = StringVar()
    
    escribe_mensaje = Label(ventana_principal, text= "ingrese un mensaje: ")
    escribe_mensaje.pack()
    ingresar_mensaje.pack()
    
    escribe_clave = Label(ventana_principal, text="ingrese una clave(si es necesario): ")
    escribe_clave.pack()
    ingresar_clave.pack()
    
    boton_repuesto_metodo_cesar= Radiobutton(Miframe, text="César", variable=metodo_seleccionado, value="César")
    boton_repuesto_metodo_atbash= Radiobutton(Miframe, text="Atbash", variable=metodo_seleccionado, value="Atbash")
    boton_repuesto_accion_cesar= Radiobutton(ventana_principal, text="Cifrar", variable=accion_seleccionada, value= "Cifrar")
    boton_repuesto_accion_atbash = Radiobutton(ventana_principal, text="Descifrar", variable=accion_seleccionada, value="Descifrar")
    
    boton_repuesto_metodo_cesar.pack()
    boton_repuesto_metodo_atbash.pack() 
    boton_repuesto_accion_cesar.pack()
    boton_repuesto_accion_atbash.pack()
    
    boton_procesar_mensaje = Button(ventana_principal, text="Procesar Mensaje", command=procesar_mensaje)
    boton_procesar_mensaje.pack()
    
    resultado =Label(ventana_principal, text="Resultado: ", font=(None, 12))
    resultado.pack()
    

    ventana_principal.mainloop()
main()
# Ventana de bienvenida
