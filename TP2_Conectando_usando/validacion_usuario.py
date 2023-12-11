def validacion_usuario(id_usuario):
    """
    >>> validacion_usuario("hola34-")
    True
    >>> validacion_usuario("gatito.23")
    True
    >>> validacion_usuario("Silvina-111")
    True
    >>> validacion_usuario("perriTO-1234567")
    True
    >>> validacion_usuario("fiuba-._89")
    True
    >>> validacion_usuario("almndfrtyhg_2345")
    False
    >>> validacion_usuario("fetjdusnt!.4")
    False
    >>> validacion_usuario("98765432")
    False
    >>> validacion_usuario("si-5")
    False
    >>> validacion_usuario("hhffhjuu")
    False
    >>> validacion_usuario("-.-----")
    False
    """
    longitud = len(id_usuario)
    caracteres_permitidos = "_-."
    letras_y_numeros = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
    tiene_letras_num = False
    tiene_caracteres_permitidos = False
    i = 0
    
    if 5 <= longitud <= 15 :
        resultado = True
    else:
        resultado = False
        
    while (resultado) and i < longitud:
        caracter = id_usuario[i]
        if caracter in letras_y_numeros :
            tiene_letras_num = True
        elif caracter in caracteres_permitidos:
            tiene_caracteres_permitidos = True
        else :
            resultado = False
        i += 1
                
    if tiene_letras_num and tiene_caracteres_permitidos :
        resultado_final = True
    else:
        resultado_final = False
    return resultado_final

import doctest
print(doctest.testmod())                
        
        
    