from tkinter import *
# autores: Alan, Maria y Silvina 
# version: 1.5 no terminada

def abrir_ventana_principal():
    # Esta funcion se encarga de eliminar la ventana de bienvenida y crear otra. En este codigo, tendrá una entrada de texto donde el usuario ingresará el mensaje que desea cifrar
    # o descifrar. También tendrá una entrada adicional para la clave de cifrado (esto se agregara segun tu solicitud). Luego mostrará el resultado cifrado o descifrado en la ventana principal.
    
    ventana_welcome.destroy()
    
    ventana_principal = Tk()
    ventana_principal.config(bg="pink")
    Miframe = Frame(ventana_principal, width=1200, height=600)
    Miframe.pack()
    ventana_principal.iconbitmap(r"elicono.ico")
    ventana_principal.title("TP Grupal Parte 1 - Grupo: Conectando")
    
    msj= StringVar() 
    clav = IntVar()
    
    escribe_mensaje = Label(Miframe, text= "ingrese un mensaje: ")
    escribe_mensaje.grid(row=0,column=0)
    
    escribe_clave = Label(Miframe, text="ingrese una clave(si es necesario): ")
    escribe_clave.grid(row=1,column=0)

    ingresar_mensaje = Entry(Miframe, textvariable= msj)
    ingresar_mensaje.grid(row=0,column=1)

    ingresar_clave = Entry(Miframe, textvariable= clav)
    ingresar_clave.grid(row=1,column=1)
    
    resultado =Label(ventana_principal, text="Resultado: ", font=(None, 12))
    resultado.pack()

    command_cifrar_cesar =lambda: resultado.config(text="Resultado: "+ cifrar_cesar(msj.get, clav.get))
    command_cifrar_atbash =lambda: resultado.config(text="Resultado: "+ cifrar_atbash(msj.get))
    command_descifrar_cesar =lambda: resultado.config(text="Resultado: "+ descifrar_cesar(msj.get, clav.get))
    command_descifrar_atbash =lambda: resultado.config(text="Resultado: "+ descifrar_atbash(msj.get))


    # Botones para cifrar y descifrar
    boton_cifrar_cesar = Button(ventana_principal, text="Cifrar mensaje César", command=command_cifrar_cesar)
    boton_cifrar_atbash = Button(ventana_principal, text="Cifrar mensaje Atbash", command=command_cifrar_atbash)
    boton_descifrar_cesar = Button(ventana_principal, text="Descifrar mensaje César", command=command_descifrar_cesar)
    boton_descifrar_atbash = Button(ventana_principal, text="Descifrar mensaje Atbash", command=command_descifrar_atbash)

    boton_cifrar_cesar.pack()
    boton_cifrar_atbash.pack()
    boton_descifrar_cesar.pack()
    boton_descifrar_atbash.pack()

    
    
    
    
    
    ventana_principal.mainloop()
    
# def obtener_valores1(mensaje,clave):
#     #Esta funcion se encarga de definir una cadena de mensaje y una clave. almacenando lo escrito en entry (msj, clav) y luego defino 
#     #la cadena para acceder a la informacion almacenada. Esta funcion la aplico en la funcion 'cifrar_cesar' y 'descifrar_cesar'
#     mensaje = msj.get()
#     Clave = clav.get()
#     return mensaje , Clave

# def obtener_valores2(mensaje):
#     #Esta funcion se encarga de definir una cadena de mensaje. almacenando lo escrito en entry (msj) y luego defino 
#     #la cadena para acceder a la informacion almacenada. Esta funcion la retorno en la funcion 'cifrar_atbash' y 'descifrar_atbash'
#     mensaje = msj.get()
#     return mensaje

    
def cifrar_cesar(mensaje, clave):
    
    TOTAL_ABECEDARIO = 26 
    TOTAL_NUMEROS = 10
    while 0 > clave or clave > TOTAL_ABECEDARIO:
        if clave < 0:
            clave += TOTAL_ABECEDARIO
        else: 
            clave -= TOTAL_ABECEDARIO
    cadena_cifrada = ""
    for caracter in mensaje :
        caracter_cifrado = ord(caracter) + clave
        if not caracter.isalnum() :
            cadena_cifrada += chr(ord(caracter))
        elif ord("z") < caracter_cifrado <= ord("z") + clave :
            cadena_cifrada += chr((caracter_cifrado) - TOTAL_ABECEDARIO)
        elif ord("Z") < caracter_cifrado <= ord("Z") + clave :
            cadena_cifrada += chr((caracter_cifrado) - TOTAL_ABECEDARIO)
        elif ord("9") < caracter_cifrado <= ord("9") + clave :
            cadena_cifrada += chr((caracter_cifrado) - TOTAL_NUMEROS)    
        else :
            cadena_cifrada += chr(caracter_cifrado)
    
        

def cifrar_atbash(mensaje):
    
    abc_minuscula = "abcdefghijklmnñopqrstuvwxyz"
    abc_mayuscula = "ZYXWVUTSRQPOÑNMLKJIHGFEDCBA"
    numeros = "0123456789"
    nuevo_mensaje = ""
    for caracter in mensaje :
        if not caracter.isalnum() :
            nuevo_mensaje += caracter
        elif caracter in abc_minuscula :
            nuevo_mensaje += abc_mayuscula[abc_minuscula.index(caracter)]
        elif caracter in abc_mayuscula :
            nuevo_mensaje += abc_minuscula[abc_mayuscula.index(caracter)]
        elif caracter in numeros :
            nuevo_mensaje += chr(ord("9") - numeros.index(caracter))
        else:
            nuevo_mensaje += caracter
    
    
def descifrar_cesar(mensaje, clave):
    
    clave_i = -clave
    cadena_descifrada = cifrar_cesar(mensaje, clave_i)
    
    
def descifrar_atbash(mensaje):
    cifrar_atbash(mensaje)
    
    
    

# Ventana de bienvenida
ventana_welcome = Tk()
ventana_welcome.config(bg="purple")
ventana_welcome.iconbitmap(r"elicono.ico")
ventana_welcome.title("TP Grupal Parte 1 - Grupo Conectando")

mensaje_bienvenida = "Bienvenido a la aplicación de mensajes secretos del grupo Conectando.\n"\
                     "Para continuar, presione continuar, de lo contrario cierre la ventana"

etiqueta_bienvenida = Label(ventana_welcome, text=mensaje_bienvenida)
etiqueta_bienvenida.pack()

boton_continuar = Button(ventana_welcome, text="Continuar", command=abrir_ventana_principal)
boton_continuar.pack()
info_grupo = Label(ventana_welcome, text="Construída por : SILVINA VILCHEZ, MARIA FERRARA, BRIAN MAMANI, NAHUEL CABRERA")
info_grupo.pack()

ventana_welcome.mainloop()
