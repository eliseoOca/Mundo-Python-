'''
Mostrar el importe del IVA de un articulo con un valor de 80 junto con
su precio final.
'''
IVA=0.21
precioBase=80
precioFinal=precioBase+(precioBase*IVA)
print(f"EL precio final es de {precioFinal}")