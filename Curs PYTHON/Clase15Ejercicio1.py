""" Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos"""
lista=[]
suma=0
for x in range(5):
    valor=float(input("Ingrese los sueldos de los 5 operarios:"))
    lista.append(valor)
    suma=suma+valor
print("Sueldos operarios:")
print(lista)
promedio=suma/5
print("el promedio de los sueldos es:")
print(promedio)