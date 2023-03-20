"""Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres."""
nombres=["pedro", "juan", "ezequiel", "pablo", "fernando"]
cantidad=0
x=0
while x<len(nombres):
    if len(nombres[x])>=5:
        cantidad=cantidad+1
    x=x+1
print("Los nombres ingresados son:")
print(nombres)
print("los nombre con ractares mayor a 5 son:")
print(cantidad)