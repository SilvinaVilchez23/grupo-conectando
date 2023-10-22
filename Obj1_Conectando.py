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
    # El objetivo de esta funcion es sustituir cada letra del "mensaje" por otra letra mediante la suma del código ASCII de determinada letra + la "clave". Separamos en 3 partes.
    # La primera si solo contiene caracteres alfabéticos, la segunda si es numerico y la tercera si no es ninguna de las anteriores, no se modifican (serian los simbolos).
    # Suele pasar que determinada letra se sustituya por un simbolo y no por una letra. En ese caso a la suma del código ASCII de determinada letra + la "clave" le restamos el total de "26" (total de las letras del abecedario). 
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
    >>> codigo_cesar ("# @ 42Jg", 1) 
    '# @ 53Kh'
    >>> codigo_cesar ("HOLA mundo", 5)
    'MTQF rzsit'
    >>> codigo_cesar ("89 ?:", 9) 
    '78 ?:'
    >>> codigo_cesar ("EjerCIciO1#", 3)
    'HmhuFLflR4#'
    >>> codigo_cesar ("*{}|/", 10) 
    '*{}|/'
    >>> codigo_cesar ("|(._.)|", 9) 
    '|(._.)|'
    
    """
    cadena_cifrada = ""
    total_abecedario = 26
    total_numeros = 10
    for caracter in mensaje :
        caracter_cifrado = (ord(caracter) + clave)
        if caracter.isalpha() :
            if ord("a") <= caracter_cifrado <= ord("z") :
                cadena_cifrada += chr(caracter_cifrado)
            elif caracter_cifrado > ord("z") :
                cadena_cifrada += chr((caracter_cifrado - total_abecedario))
            elif ord("A") <= caracter_cifrado <= ord("Z") :
                cadena_cifrada += chr(caracter_cifrado)
            elif caracter_cifrado > ord("Z") :
                cadena_cifrada += chr((caracter_cifrado - total_abecedario))
        elif caracter.isnumeric() :
            if ord("0") <= caracter_cifrado <= ord("9") :
                cadena_cifrada += chr(caracter_cifrado)
            elif caracter_cifrado > ord("9") :
                cadena_cifrada += chr((caracter_cifrado - total_numeros))
        else:
            cadena_cifrada += chr(ord(caracter))
        
        
    return cadena_cifrada

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
          
            
            
    