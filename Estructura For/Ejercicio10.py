num = int(input("Ingrese un número: "))
primo = True

for i in range(1, num + 1):
    if i == 1:
        print(f"El numero {i} no es primo")
    else:
        numero = i
        for j in range(2, numero):
            if numero % j == 0:
                primo = False
                break
        else:
            primo = True

        if primo:
            print(f"El numero {i} es primo")
        else:
            print(f"El numero {i} no es primo")