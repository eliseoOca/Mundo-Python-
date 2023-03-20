def cuentaPalabras(texto):
    palabras= texto.split(" ")
    palabrasContadas={}
    contador=0
    longitud= len(palabras)
    for x in range (0, longitud):
        primera = palabras[x]
        #print(primera)
        for z in range (0, longitud):
            segunda = palabras[z]
            if primera == segunda:
                contador+=1
        palabrasContadas[primera]= contador
        contador=0
    return palabrasContadas
try:
    fichero=open("EjercicioCUENTApalabras.txt","r",encoding='utf-8')
    texto=fichero.read()
    #print("fichero leido")
    #fichero.close()
except:
    print("No se ha podido leer el archivo")
finally:
    #print("Archivo cerrado")
    fichero.close()
texto=input("Pasame palabras o textos para contar sus palabras: ")
#texto="Ejemplo de texto, ejemplo de texto"
cuentaPalabras=cuentaPalabras(texto)
print(cuentaPalabras)