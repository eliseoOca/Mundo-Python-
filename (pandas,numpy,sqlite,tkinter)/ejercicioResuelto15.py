'''Definir una funcion que calcule la suma y multiplicacion de una lista'''
def suma(lista):
    suma=0
    for x in lista:
        suma +=x
    return suma

def multiplicar(lista):
    multiplicacion=1
    for x in lista:
        multiplicacion*=x
    return multiplicacion
lista=[1,32,53,45,67,89,76,56,3]
print(suma(lista))
print(multiplicar(lista))