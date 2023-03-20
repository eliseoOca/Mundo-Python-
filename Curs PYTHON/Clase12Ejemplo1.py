"""
  Realizar la carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el nombre de la persona con mayor altura.
"""

print("Datos de la primer persona")
nombre1=input("Ingrese nombre:")
edad1=int(input("Ingrese edad:"))
altura1=float(input("Ingrese altura:"))
print("Datos de la segunda persona")
nombre2=input("Ingrese nombre:")
edad2=int(input("Ingrese edad:"))
altura2=float(input("Ingrese altura:"))
print("La persona mas alta es:")
if altura1>altura2:
    print(nombre1)
else:
    print(nombre2)