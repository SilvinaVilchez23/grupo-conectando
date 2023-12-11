def codigo_cesar(mensaje, clave) :
    # El objetivo de esta funcion es sustituir cada letra del "mensaje" por otra letra mediante la suma del código ASCII de determinada letra + la "clave". Es distinto para mayusculas y minusculas.
    # Suele pasar que determinada letra se sustituya por un simbolo y no por una letra. En ese caso a la suma del código ASCII de determinada letra + la "clave" le restamos el total de "26" (total de las letras del abecedario)
    # Lo mismo hacemos con los numeros. Los simbolos no se modifican. 
    # Autor : Silvina y Brian
    """
    >>> codigo_cesar ("%&2345Pm ", 3)
    '%&5678Sp '
    >>> codigo_cesar ("EJERCICIO", 3)
    'HMHUFLFLR'
    >>> codigo_cesar ("ejercicio", 2)
    'glgtekekq'
    >>> codigo_cesar ("1 23456789", 4)
    '5 67890123'
    >>> codigo_cesar ("EJERCICIO", 8)
    'MRMZKQKQW'
    >>> codigo_cesar("EJERCICIO", 77)
    'DIDQBHBHN'
    >>> codigo_cesar ("ejercicio", -52)
    'ejercicio'
    >>> codigo_cesar ("HOLA mundo", 31)
    'MTQF rzsit'
    >>> codigo_cesar ("89 ?:", 9) 
    '78 ?:'
    >>> codigo_cesar ("EjerCIciO1#", 3)
    'HmhuFLflR4#'
    >>> codigo_cesar ("*{}|/", 18) 
    '*{}|/'
    >>> codigo_cesar ("|(._.)|", 9) 
    '|(._.)|'
    

    """
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
        
                    
    return cadena_cifrada
    
import doctest
print(doctest.testmod())
