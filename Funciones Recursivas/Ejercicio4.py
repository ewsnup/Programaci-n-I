def calcular_numero_fibonacci(numero:int)->int:
    if numero == 0 or numero == 1:
        return numero
    else:
        return calcular_numero_fibonacci (numero - 1) + calcular_numero_fibonacci (numero - 2)

numero = int(input("Ingrese un numero: "))

print(calcular_numero_fibonacci(numero))