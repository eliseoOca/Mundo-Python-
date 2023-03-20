def cuentaVocales(texto):
    vocales = 'aeiou'
    contador= 0
    longitud = len(texto)
    for x in range(longitud):
        letra=texto.lower()[x]
        if letra in vocales:
            contador+=1
    return contador
    
texto = input("iNGRESE UN TEXTO: ")
contador=cuentaVocales(texto)
print(f"el numero de vocales de la cadena {texto} es igual a {contador}")