'''Solicitar una lista al usuario,ordenarla e indicar con otras listas
los numero pares e impares'''
def solicitar():
    lista = []
    num=None
    while num != 0:
        num = int(input("Dime un numero: (0 para terminar) : "))
        if num >= 0:
            lista.append(num)
        elif num == 0:
            break
        else:
            print("El numero debe mayor que 0")
    return lista

def ordenar(lista):
    lista.sort()
    pares=[]
    impares=[]
    for x in lista:
        if x%2==0:
            pares.append(x)
        else:
            impares.append(x)
    return pares, impares
#print(solicitar())
lista=solicitar()
print("Impremimos la lista")
print(lista)
pares,impares=ordenar(lista)
print("imprimimos la lista de numero pares")
print(pares)
print("Imprimimos la lis de numeros pares")
print(impares)