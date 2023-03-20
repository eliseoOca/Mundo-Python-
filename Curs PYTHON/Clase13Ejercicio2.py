"""Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. 
Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal."""

oracion=input("Ingresa una oracion: ")
oracion2=oracion.lower()
print(oracion2)
cantidad=0
x=0
while x<len(oracion2):
    if oracion2[x]=="a" or oracion2[x]=="e" or oracion2[x]=="i" or oracion2[x]=="o" or oracion2[x]=="u":
        cantidad=cantidad+1
    x=x+1
print("la cantidad de vocales es")
print(cantidad)
