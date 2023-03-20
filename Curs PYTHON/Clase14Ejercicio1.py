"""Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100."""
lista=[1, 2, 3, 4, 5, 6, 7, 8]
cantidad=0
x=0
while x<len(lista):
    if lista[x]>100:
        cantidad=cantidad+1
    x=x+1
print("La lista esta constituida por los elemnetos:")
print(lista)
print("La cantidad de valores mayores a 100 en la lista son:")
print(cantidad)