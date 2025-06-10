def determinar_par(numero:int):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
        

numero = int(input("Ingrese un número: "))
determinar_par(numero)
