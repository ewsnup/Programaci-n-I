def encontrar_numero_maximo(num1:int, num2:int, num3:int)->int:
    return max(num1, num2, num3)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

num_mayor = encontrar_numero_maximo(num1, num2, num3)
print("El número mayor es:", num_mayor)
