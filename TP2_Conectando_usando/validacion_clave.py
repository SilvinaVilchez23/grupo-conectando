def validacion_clave(clave_usuario) :
    """
    >>> validacion_clave("GTc5*")
    True
    >>> validacion_clave("Kau#s2")
    True
    >>> validacion_clave("_oYbs1")
    True
    >>> validacion_clave("qwDa4")
    False   
    >>> validacion_clave("Am2*")
    True
    >>> validacion_clave("Solcito3#")  
    False
    >>> validacion_clave("PUM3#")
    False
    >>> validacion_clave("aty4*")
    False
    >>> validacion_clave("54")  
    False
    >>> validacion_clave("Zoofg2")   
    False
    """
    longitud_valida = 4 <= len(clave_usuario) <= 8
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False
    caracteres_repetidos = False
    i = 0
    
    if longitud_valida:
        resultado = True
    else:
        resultado = False

    
    while (resultado) and i < len(clave_usuario) - 1 and not caracteres_repetidos:
        caracter_actual = clave_usuario[i]
        caracter_siguiente = clave_usuario[i + 1]

        # Verificar caracteres repetidos adyacentes
        if caracter_actual == caracter_siguiente:
            caracteres_repetidos = True

        if caracter_actual.isupper():
            tiene_mayuscula = True
        elif caracter_actual.islower():
            tiene_minuscula = True
        elif caracter_actual.isdigit():
            tiene_numero = True
        elif caracter_actual in "_-#*":
            tiene_caracter_especial = True

        i += 1

    # Verificar el último carácter de la clave
    ultimo_caracter = clave_usuario[-1]
    if ultimo_caracter.isupper():
        tiene_mayuscula = True
    elif ultimo_caracter.islower():
        tiene_minuscula = True
    elif ultimo_caracter.isdigit():
        tiene_numero = True
    elif ultimo_caracter in "_-#*":
        tiene_caracter_especial = True

    # Verificar al menos una letra mayúscula, una letra minúscula, un número y un caracter especial
    condiciones_cumplidas = tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial

    # Devolver True solo si todas las condiciones son verdaderas
    if condiciones_cumplidas and not caracteres_repetidos:
        resultado_final = True
    else:
        resultado_final = False
    return resultado_final


if __name__ == '__main__':
    import doctest
    doctest.testmod()            
            