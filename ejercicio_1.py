"""El cifrado de César sustituye cada letra del mensaje por otra. La letra sustituida se obtiene
“desplazando” cada letra del abecedario una cierta cantidad de posiciones a la derecha. Esta
cantidad de lugares que una letra se desplaza es la clave secreta que se debe pasar al receptor del
mensaje para poder descifrarlo.
Consideraciones
● Se deben considerar tanto las letras mayúsculas como minúsculas.
● Adapte el método para encriptar de forma similar los dígitos numéricos que pueda tener el
mensaje.
● Los espacios y otros símbolos no se codifican, quedan igual.
● Sugerimos que lean sobre las funciones ord() y chr(). Cada letra tiene asignado un código
numérico (llamado código ASCII) y letras consecutivas tienen números consecutivos."""

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
    
    """
    cadena_cifrada = ""
    total_abecedario = 26
    total_numeros = 10
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
 
    
