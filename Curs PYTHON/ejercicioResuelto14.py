'''Definir una funcion que calcule la longitud de una cadena dada'''
def longitudCadena(cadena):
    x=0
    for elemento in cadena:
        x+=1
    return x
print(longitudCadena("Eliseo"))