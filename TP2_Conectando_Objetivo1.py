from tkinter import *
import validacion_usuario as validar_usuario
import validacion_clave as validar_clave
from tkinter import messagebox
import csv
import Cifrado_Atbash as cifrar_atbash
import Cifrado_Cesar as cifrar_cesar # cambiar codigo cesar por el mod
import Cifrado_Cesar as descifrar_cesar 

def main() :
    # funcion que crea la ventana principal donde se encuentra los dos botones: "Crear Usuario" e "Ingreso Usuario".
    ventana_welcome = Tk()
    ventana_welcome.config(bg="purple")
    ventana_welcome.iconbitmap(r"icono.ico")

    ventana_welcome.title("TP Grupal Parte 1 - Grupo Conectando")

    mensaje_bienvenida = "Bienvenido a la aplicación de mensajes secretos del grupo Conectando.\n"\
                    "Para continuar, presione continuar, de lo contrario cierre la ventana"

    etiqueta_bienvenida = Label(ventana_welcome, text=mensaje_bienvenida)
    etiqueta_bienvenida.pack()

    boton_crear_usuario = Button(ventana_welcome, text="crear usuario", command=ventana_creacion_usuario)
    boton_crear_usuario.pack()
    
    boton_ingreso_usuario = Button(ventana_welcome, text="ingreso usuario", command=lambda:abrir_identificacion_para_acceso(ventana_welcome))
    boton_ingreso_usuario.pack()
    
    info_grupo = Label(ventana_welcome, text="Construída por : SILVINA VILCHEZ, MARIA FERRARA, BRIAN MAMANI, NAHUEL CABRERA")
    info_grupo.pack()
    ventana_welcome.mainloop()
# ------------------------------------------------------------------------------------------------------------------------

def ventana_creacion_usuario(): 
    # funcion que crea la ventana de creacion de usuario.
    def funcion_creacion_usuario() :
        # Función para crear un nuevo usuario.
        id_usuario = ingresar_id_usuario.get()
        clave_usuario = ingresar_clave_usuario.get()
        guardar_pregunta = marcar_pregunta.get()
        guardar_respuesta = ingresar_respuesta.get()

        # Validar el identificador del usuario.
        if not validar_usuario.validacion_usuario(id_usuario):
            messagebox.showerror("Error", "Identificador no válido")
            return

        # Validar la clave del usuario.
        if not validar_clave.validacion_clave(clave_usuario):
            messagebox.showerror("Error", "Clave no válida")
            return
        # checkeo que no sea un usuario existente.
        if checkeo_usuario(id_usuario):
            messagebox.showerror("Error", "Identificador en uso")
            return

        # Guardo los datos del nuevo usuario en el archivo CSV.
        salvar_usuario([id_usuario, clave_usuario, guardar_pregunta, guardar_respuesta, 0])

        messagebox.showinfo("Éxito", "Usuario creado correctamente")
        
    ventana_crear = Tk()
    ventana_crear.title("Sistema de Registro de Usuarios")
    ventana_crear.iconbitmap(r"icono.ico")
     
    preguntas = cargando_preguntas()


    label_id_usuario = Label(ventana_crear, text="Identificador:")
    label_id_usuario.grid(row=0, column=0, sticky="e")

    ingresar_id_usuario = Entry(ventana_crear)
    ingresar_id_usuario.grid(row=0, column=1, pady=5)

    label_clave_usuario = Label(ventana_crear, text="Clave:")
    label_clave_usuario.grid(row=1, column=0, sticky="e")

    ingresar_clave_usuario = Entry(ventana_crear, show="*")
    ingresar_clave_usuario.grid(row=1, column=1, pady=5)

    label_pregunta = Label(ventana_crear, text="Pregunta de recuperación:")
    label_pregunta.grid(row=2, column=0, sticky="e")
    
    # tengo que corregir el archivo de usuario y que en vez que quede guardada la pregunta textual quede el id de la pregunta

    marcar_pregunta = StringVar(ventana_crear)
    marcar_pregunta.set(preguntas[0])
    
   
    # Opciones de la pregunta de recuperación.

    menu_prepguntas = OptionMenu(ventana_crear, marcar_pregunta, *preguntas)
    menu_prepguntas.grid(row=2, column=1, pady=5)

    label_guardar_respuesta = Label(ventana_crear, text="Respuesta de recuperación:")
    label_guardar_respuesta.grid(row=3, column=0, sticky="e")

    ingresar_respuesta = Entry(ventana_crear)
    ingresar_respuesta.grid(row=3, column=1, pady=5)

    boton_registrar = Button(ventana_crear, text="Registrar", command=funcion_creacion_usuario)
    boton_registrar.grid(row=4, column=1, pady=10)

    ventana_crear.mainloop()
    
def cargando_preguntas():
    # funcion que crea una lista con las preguntas.
    preguntas = []
    with open("preguntas.csv", "r") as file:
        reader = csv.reader(file)
        for fila in reader:
            preguntas.append(fila[1])
    return preguntas
                
def salvar_usuario(user_data):
    # funcion que guarda los nuevos usuarios ingresados.
    with open("usuarios.csv", "a", newline="") as archivo:
        escribo = csv.writer(archivo)
        escribo.writerow(user_data)
        
        
def checkeo_usuario(id_usuario):
    # funcion que checkea si el iterable es verdadero o falso.
    with open("usuarios.csv", "r") as archivo:
        leo = csv.reader(archivo)
        return any(row and row[0] == id_usuario for row in leo)
    
# -----------------------------------------------------------------------------------------------------
def abrir_identificacion_para_acceso(main) :
    # es una funcion que crea una ventana para acceder a un usuario ya creado donde se encuentran la posibilidad de ingresar sin problema o 
    # recuperar la clave en caso de olvidarla.
    main.destroy()
    nueva_ventana_identificacion_acceso = Tk()
    nueva_ventana_identificacion_acceso.config(bg="purple")
    nueva_ventana_identificacion_acceso.iconbitmap(r"icono.ico")
    nueva_ventana_identificacion_acceso.title("Identificación para acceso")

    
    label_usuario_creado = Label(nueva_ventana_identificacion_acceso,text = "Ingresar Usuario:")
    label_usuario_creado.pack()

    ingresar_usuario_creado= Entry(nueva_ventana_identificacion_acceso)
    ingresar_usuario_creado.pack()

    label_clave_creada = Label(nueva_ventana_identificacion_acceso,text = "Ingresar Clave:")

    ingresar_clave_creada= Entry(nueva_ventana_identificacion_acceso,show="*")
    label_clave_creada.pack()
    
    ingresar_clave_creada.pack()

    boton_ingreso = Button(nueva_ventana_identificacion_acceso,text= "Ingresar", command=lambda:entrar(ingresar_usuario_creado.get(), ingresar_clave_creada.get(), nueva_ventana_identificacion_acceso))
    boton_ingreso.pack()
    
    boton_recuperar = Button(nueva_ventana_identificacion_acceso, text="recuperacion de clave", command=lambda:recuperacion_clave_ventana(ingresar_usuario_creado.get()))
    boton_recuperar.pack()
# -----------------------------------------------------------------------------------------------------------------
def entrar(datos_usuario, clave_usuario, abrir_identificacion_para_acceso) :
    # funcion que se encarga de verificar si es un usuario registrado. bloquea al usuario en caso de que tenga 
    # mas de 3 intentos fallidos de recuperacion de clave.
    intentos = guardar_intentos(datos_usuario)
    if checkeo_usuario(datos_usuario) and validar_clave.validacion_clave(clave_usuario) and intentos <3:
        messagebox.showinfo("exito", "ingreso exitoso")
        abrir_identificacion_para_acceso.destroy()
        return procesar_validez_usuario()
        
        
        # remitente = checkeo_usuario(datos_usuario[0])
        

    elif intentos >= 3:
        messagebox.showwarning("Advertencia", "Usuario bloqueado") 
        return
           
    else:
        messagebox.showerror("error", "Identificador inexistente o clave errónea\n"
                             "Si no estás registrado, regístrate previamente.\n"
                             "Si olvidaste la clave, presiona el botón recuperar clave.")
# ---------------------------------------------------------------------------------------------------------------------
def recuperacion_clave_ventana(datos_usuario):
    # funcion que crea una ventana de recuperacion de clave.
    intentos = guardar_intentos(datos_usuario)

    if intentos >= 3:
        messagebox.showwarning("Advertencia", "Usuario bloqueado")
        return
    
    ventana_recuperacion_clave = Tk()
    ventana_recuperacion_clave.config(bg="purple")
    ventana_recuperacion_clave.iconbitmap(r"icono.ico")
    ventana_recuperacion_clave.title("recuperacion clave")

    
    pregunta_guardada_id = (cargar_dato_usuario(datos_usuario)[2])
    pregunta_texto = pregunta_guardada_id
    
    pregunta_recuperacion = Label(ventana_recuperacion_clave, text=f"pregunta de recuperacion : {pregunta_texto}")
    ingresar_respuesta = Entry(ventana_recuperacion_clave)
    pregunta_recuperacion.pack()
    ingresar_respuesta.pack()
    
    boton_recuperacion = Button(ventana_recuperacion_clave, text="recuperar", command=lambda:funcion_recuperar(datos_usuario, ingresar_respuesta.get()))  
    boton_recuperacion.pack()  
    ventana_recuperacion_clave.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------   

def funcion_recuperar(datos_usuario, respuesta_ingresada):
   # funcion para recuperar la clave .
    with open("usuarios.csv", "r") as file:
        # abre el archivo de usuarios y lee fila por fila. Si en determinada fila el "datos_usuario" corresponde 
        # con el usuario guardado en la fila y ademas la "respuesta_ingresada" corresponde con la respuesta guarada
        # saldra un mensaje mostrandote la clave olvidada y re reseteara los intentos fallidos.
        reader = csv.reader(file)
        for fila in reader:
            if fila[0] == datos_usuario and fila[3] == respuesta_ingresada:
                messagebox.showinfo("recuperacion exitoso", f"tu clave es: {fila[1]}")
                reseteo_intentos(datos_usuario) 
                return 
    
    # Registrar intento de recuperación fallido.
    with open("recuperacion.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datos_usuario, 1])
        messagebox.showerror("error", "respuesta incorrecta")
        incremento_intentos(datos_usuario) 

def cargar_dato_usuario(datos_usuario):
    # funcion que devuelve toda la info de una fila.
    with open("usuarios.csv", "r") as archivo:
        linea = csv.reader(archivo)
        for fila in linea:
            if fila and fila[0] == datos_usuario:
                return fila
    return None

def incremento_intentos(datos_usuario):
    # funcion que vigila los intentos ingresados, si es igual o se pasa de 3 intentos fallidos, bloquea al usuario mediante
    # un mensaje.
    intentos = guardar_intentos(datos_usuario) + 1
    set_intentos(datos_usuario, intentos)

    if intentos >= 3:
        
        messagebox.showwarning("Advertencia", "Usuario bloqueado")
        
def guardar_intentos(datos_usuario):
    # funcion que guarda los intentos en el archivo "recuperacion".
    with open("recuperacion.csv", "r") as archivo:
        linea = csv.reader(archivo)
        for columna in linea:
            if columna and columna[0] == datos_usuario:
                return int(columna[1])
    return 0

def set_intentos(datos_usuario, intentos):
    # funcion que actualiza los intentos mediante el usuario y los intentos guardados.
    dato = []
    with open("recuperacion.csv", "r") as archivo:
        linea = csv.reader(archivo)
        for fila in linea:
            if fila and fila[0] == datos_usuario:
                fila[1] = str(intentos)
            dato.append(fila)

    with open("recuperacion.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(dato)

def reseteo_intentos(datos_usuario):
    # funcion que resetea y vuelve a 0 el numero de intentos.
    set_intentos(datos_usuario, 0)
# ------------------------------------------------------------------------------------------------------------------

def ventana_mensaje_cesar_atbash():
    # funcion que crea una ventana para envios a usuarios validos.
    ventana_mensaje = Tk()
    ventana_mensaje.config(bg="purple")
    ventana_mensaje.iconbitmap(r"icono.ico")
    ventana_mensaje.title("envios de mensajes cifrados mediante el codigo cesar")
    
    
    label_envio = Label(ventana_mensaje, text="enviar a(para enviar a todos los usuarios escriba '*') : ")
    label_envio.grid(row=0, column=0)
    
    ingresar_destinatario = Entry(ventana_mensaje)
    ingresar_destinatario.grid(row=0, column=1)
    
    boton_de_envio = Button(ventana_mensaje, text="enviar", command=lambda:checkear_usuario_ventana(ingresar_destinatario.get(), ventana_mensaje))
    boton_de_envio.grid(pady=10, padx=10, column=1)
    
def obtengo_usuarios():
    usuarios_all = []
    # funcion que checkea si el iterable es verdadero o falso.
    with open("usuarios.csv", "r") as archivo:
        linea = csv.reader(archivo)
        for fila in linea:
            usuarios_all.append(fila[0])
        return usuarios_all                        
        
def checkear_usuario_ventana(destinatario_ingresado, ventana_mensaje_cesar_atbash):
    # funcion que revisa si es un destinatario valido o no.
    destinatario_valido = checkeo_usuario(destinatario_ingresado)

    if destinatario_valido:
        ventana_mensaje_cesar_atbash.destroy()

    elif destinatario_ingresado  == "*":
        ventana_mensaje_cesar_atbash.destroy()
        
    else:
        messagebox.showwarning("error", "destinatario inexistente")
        
def procesar_validez_usuario():
    ventana_ingresar_mensaje = Tk()
    ventana_ingresar_mensaje.config(bg="purple")
    ventana_ingresar_mensaje.iconbitmap(r"icono.ico")
    ventana_ingresar_mensaje.title("mensajes mediante el codigo cesar")
    
    def procesar_mensaje():
          
        mensaje = ingresar_mensaje.get()
        metodo = metodo_seleccionado.get()
        clave = ingresar_clave.get()
        if metodo == "César":
            metodo = "c" + clave
            
            clave = int(clave)          
            if accion_seleccionada.get() == "Cifrar":
                
                mensaje_cifrado = cifrar_cesar.codigo_cesar(mensaje, clave)
                resultado.config(text="Resultado: " + mensaje_cifrado) 
            else:
                mensaje_cifrado = descifrar_cesar.codigo_cesar(mensaje, -clave)  # Descifrado con clave -N
                resultado.config(text="Resultado: " + mensaje_cifrado)
        else:
            metodo = "a" + clave
    
            mensaje_cifrado = cifrar_atbash.Cifrado_Atbash(mensaje)  # Cifrado o descifrado con Atbash
            
            
        resultado.config(text="Resultado: " + mensaje_cifrado)
        salvar_mensaje([metodo, mensaje_cifrado])

        
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
    
    boton_enviar_mensaje_cifrado_cesar = Button(ventana_ingresar_mensaje, text="Enviar mensaje cifrado César", command=ventana_mensaje_cesar_atbash)
    boton_enviar_mensaje_cifrado_atbash = Button(ventana_ingresar_mensaje, text= "Enviar mensaje cifrado Atbash", command=ventana_mensaje_cesar_atbash)
    
    boton_enviar_mensaje_cifrado_cesar.pack()
    boton_enviar_mensaje_cifrado_atbash.pack()
    boton_repuesto_metodo_cesar.pack()
    boton_repuesto_metodo_atbash.pack()
    boton_repuesto_accion_cesar.pack()
    boton_repuesto_accion_atbash.pack()
    
    boton_procesar_mensaje = Button(ventana_ingresar_mensaje, text="Procesar Mensaje", command=procesar_mensaje)
    boton_procesar_mensaje.pack()
    
    resultado =Label(ventana_ingresar_mensaje, text="Resultado: ", font=(None, 12))
    resultado.pack()
    
def salvar_mensaje(datos_de_usuario):
    with open("mensajes.csv", "a", newline= "") as archivo_final:
        writer = csv.writer(archivo_final)
        
        writer.writerow(datos_de_usuario)
        messagebox.showinfo("exito", "mensaje enviado")
        
                    
            
main()