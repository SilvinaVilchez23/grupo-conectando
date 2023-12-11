def Cifrado_Atbash (mensaje):
    """
    >>> Cifrado_Atbash ("HOLA MUNDO")
    'sloz ñfnwl'
    >>> Cifrado_Atbash ("hola mundo")
    'SLOZ ÑFNWL'
    >>> Cifrado_Atbash ("SLOZ ÑFNWL")
    'hola mundo'
    >>> Cifrado_Atbash ("AbCdEfG")
    'zYxWvUt'
    >>> Cifrado_Atbash ("238129")
    '761870'
    >>> Cifrado_Atbash ("HOla5 1muNDo7")
    'slOZ4 8ÑFnwL2'
    >>> Cifrado_Atbash ("@#?!-")
    '@#?!-'
    >>> Cifrado_Atbash ("EJERCICIO2@€%ejercicio2@€%")
    'vqvixrxrl7@€%VQVIXRXRL7@€%'
    >>> Cifrado_Atbash ("abcdefghijklmnñopqrstuvwxyz")
    'ZYXWVUTSRQPOÑNMLKJIHGFEDCBA'
    >>> Cifrado_Atbash ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    'zyxwvutsrqpoñnmlkjihgfedcba'
    """
    
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
    return nuevo_mensaje

if __name__ == '__main__':
    import doctest
    doctest.testmod()
