total = 0
promedio = 0


for i in range(10):
    num = int(input("Ingrese un número: "))
    print("El numero que usted ingresó es el: ", num)
    total = total + num
    if num == 0:
        break

if i != 0:
    promedio = total / i

print("promedio de los numeros ingresados es: ", promedio)
print("la suma de los numeros ingresados es: ", total)