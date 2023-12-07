
def Cifrado_Atbash (mensaje):
    
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

