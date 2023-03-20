"""Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos. """

sueldosman=[]
print("Sueldos turno manana")
for x in range(4):
    valor=float(input("Ingrese sueldo:"))
    sueldosman.append(valor)

sueldostar=[]
print("Sueldos turno tarde")
for x in range(4):
    valor=float(input("Ingrese sueldo:"))
    sueldostar.append(valor)

print("Turno manana")
print(sueldosman)
print("Turno tarde")
print(sueldostar)