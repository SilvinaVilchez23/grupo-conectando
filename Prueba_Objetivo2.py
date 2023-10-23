""" Objetivo 2: Cifrado Atbash
➔ Escribir una función que reciba el mensaje a cifrar (cadena de caracteres), y devuelva el
mensaje cifrado, mediante el cifrado atbash. Probarla utilizando doctest, con al menos 10
casos diferentes.
Este cifrador también reemplaza cada letra por otra pero en este caso en lugar de un
desplazamiento se utiliza la versión invertida del abecedario. En nuestro caso, además
cambiaremos mayúsculas por minúsculas, y viceversa. """

def cifrar (mensaje):
    
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    abc_mayus = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    numeros = "0123456789"

    nuevo_mensaje = ""
    for caracter in mensaje :
        
        

        if not caracter.isalnum() :
            nuevo_mensaje += caracter

        elif caracter in abecedario :
            nuevo_mensaje += abc_mayus[abecedario.index(caracter)]

        elif caracter in abc_mayus :
            nuevo_mensaje += abecedario[abc_mayus.index(caracter)]

        elif caracter in numeros :
            nuevo_mensaje += chr(ord("9") - numeros.index(caracter))



        else :
           nuevo_mensaje += caracter
        
                    
    return nuevo_mensaje

print(cifrar("abcdef9"))
print(cifrar("ABCDEF0"))
