"""Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error."""

clave=input("Ingrese clave que tenga entra 10 y 20 caracteres: ")
if len(clave)>=10 and len(clave)<=20:
    print("Clave correcta")
else:
    print("Clave incorrecta")