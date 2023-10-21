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
    for caracter in mensaje :
        if caracter.islower() :
            if ord(caracter) + clave > ord("z") :
                cadena_cifrada += chr((ord(caracter) + clave) - 26) 
            else:
                cadena_cifrada += chr(ord(caracter) + clave)
        if caracter.isupper() :
            if ord(caracter) + clave > ord("Z") :
                cadena_cifrada += chr((ord(caracter) + clave) - 26)
            else:
                cadena_cifrada += chr(ord(caracter) + clave)  
        if caracter.isnumeric() :
            if ord(caracter) + clave > ord("9") :
                cadena_cifrada += chr((ord(caracter) + clave) - 10)
            else:
                cadena_cifrada += chr(ord(caracter) + clave)
            
        if 32 <= ord(caracter) <= 47 :
            cadena_cifrada += chr(ord(caracter))
            
             
                
    return cadena_cifrada
import doctest
print(doctest.testmod())            
            
            
    