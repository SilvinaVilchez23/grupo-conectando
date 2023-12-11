def codigo_cesar(mensaje, clave):
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
    cadena_cifrada = ""
    mayuscula_a = 65
    minuscula_a = 97
    total_abc = 26
    total_num = 10
    
    for caracter in mensaje:
        if (caracter.isalpha()) :
            if (caracter.islower()):
                cadena_cifrada += chr((ord(caracter) + clave - minuscula_a) % total_abc + minuscula_a)
            else:
                cadena_cifrada += chr((ord(caracter) + clave - mayuscula_a) % total_abc + mayuscula_a)
        elif (caracter.isdigit()) :
            cadena_cifrada += str((int(caracter) + clave) % total_num)  
            
        else:
            cadena_cifrada += caracter
            
        
    return (cadena_cifrada)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()