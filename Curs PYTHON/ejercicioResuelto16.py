'''Definir funcion que muestre una cadena al reves'''
def cadenaReves(palabra):
    alreves=""
    contador = len(palabra)
    indice=-1
    while contador>=1:
        alreves+=palabra[indice]
        indice=indice + (-1)
        contador-=1
    return alreves
print(cadenaReves("Hola soy un Estudiante "))