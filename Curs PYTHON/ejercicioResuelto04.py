'''
el ordenador piensa un numero y el usuario tiene que adivinarlo,
muestra tambien el numero de intentos.
'''
from random import randint as azar
piensaNumeor=azar(1,100)
numeroUsuario=int(input("Adivina el numero: "))
intentos=0
continua=True
while(continua):
    if numeroUsuario < piensaNumeor:
        print("El numero que tengo es mayor")
        intentos=intentos+1
        numeroUsuario=int(input("Adivina el numero: "))
    elif numeroUsuario>piensaNumeor:
        print("El numero que eh pensado es menor")
        intentos=intentos+1
        numeroUsuario=int(input("Adivina el numero: "))
    else:
        print("Adivinaste !!!")
        print("El numero de intentos es "+str(intentos))
        print("Quieres continuar (s/n)?")
        continuar=input()
        if(continuar=="s"or continuar=="S"):
            continua= True
            intentos=0
            piensaNumeor=azar(1,100)
            numeroUsuario=int(input("Adivina el numero: "))
        else:
            continua=False

print("Fuera del juego")