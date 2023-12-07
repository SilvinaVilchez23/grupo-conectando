from tkinter import *
import Cifrado_Atbash as cifrar_atbash
import cifrado_cesar as cifrar_cesar
import cifrado_cesar as descifrar_cesar 

def procesar_validez_usuario():
    ventana_ingresar_mensaje = Tk()
    ventana_ingresar_mensaje.config(bg="purple")
    ventana_ingresar_mensaje.iconbitmap(r"icono.ico")
    ventana_ingresar_mensaje.title("mensajes mediante el codigo cesar")
    ventana_ingresar_mensaje.geometry("100x60")

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
    
    ingresar_mensaje = Entry(ventana_ingresar_mensaje, width=40)
    ingresar_clave = Entry(ventana_ingresar_mensaje, width=40)
    
    Miframe = Frame(ventana_ingresar_mensaje)
    Miframe.pack()
    
    seleccion = Label(Miframe, text="Seleccione el método:")
    seleccion.pack()
    
    accion_seleccionada = StringVar()
    
    escribe_mensaje = Label(ventana_ingresar_mensaje, text= "ingrese un mensaje: ")
    escribe_mensaje.pack()
    ingresar_mensaje.pack()
    
    escribe_clave = Label(ventana_ingresar_mensaje, text="ingrese una clave(si es necesario): ")
    escribe_clave.pack()
    ingresar_clave.pack()
    
    boton_repuesto_metodo_cesar= Radiobutton(Miframe, text="César", variable=metodo_seleccionado, value="César")
    boton_repuesto_metodo_atbash= Radiobutton(Miframe, text="Atbash", variable=metodo_seleccionado, value="Atbash")
    boton_repuesto_accion_cesar= Radiobutton(ventana_ingresar_mensaje, text="Cifrar", variable=accion_seleccionada, value= "Cifrar")
    boton_repuesto_accion_atbash = Radiobutton(ventana_ingresar_mensaje, text="Descifrar", variable=accion_seleccionada, value="Descifrar")
    
    boton_repuesto_metodo_cesar.pack()
    boton_repuesto_metodo_atbash.pack()
    boton_repuesto_accion_cesar.pack()
    boton_repuesto_accion_atbash.pack()
    
    boton_procesar_mensaje = Button(ventana_ingresar_mensaje, text="Procesar Mensaje", command=procesar_mensaje)
    boton_procesar_mensaje.pack()
    
    resultado =Label(ventana_ingresar_mensaje, text="Resultado: ", font=(None, 12))
    resultado.pack()
    
    ventana_ingresar_mensaje.mainloop()
procesar_validez_usuario()
    

    
