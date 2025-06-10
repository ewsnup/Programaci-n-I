num = int(input("Ingrese un número: "))

divisores = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(i) 
        divisores += 1

print("El número de divisores encontrados es:", divisores)