'''dada una cadena indicar si es palindromo o no'''
palabra=input("Dime una palabra: ")
palabraAlreves=palabra[::-1]
print(palabra)
print(palabraAlreves)
if(palabra==palabraAlreves):
    print("Es palidromo")
else:
    print("No es palindromo")