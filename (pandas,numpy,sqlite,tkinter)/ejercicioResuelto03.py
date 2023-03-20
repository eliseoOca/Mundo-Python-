#Mostrar los numeros pares en un intervalo dade 
# como del 1 al 50 y contar cuantos son.
cuenta=0
print("Numero pares ")
for x in range(1,51):
    if(x%2==0):
        print(x)
        cuenta=cuenta+1
print(f"Tenemos {cuenta} numero pares")
