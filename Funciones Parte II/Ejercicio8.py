def todos_los_primos(unidad: int, limite: int) -> int:
    cant_primos = 0
    
    for i in range(unidad, limite + 1):
        if i == 1:
            print(f"El número {i} no es primo")

            print(f"El número {i} no es primo")
        else:
            primo = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    primo = False
                    break

            if primo:
                print(f"El número {i} es primo")
                cant_primos += 1  
            else:
                print(f"El número {i} no es primo")
    
    return cant_primos


num = int(input("Ingrese un número: "))  
cantidad_primos = todos_los_primos(1, num)  
print(f"Cantidad de números primos encontrados: {cantidad_primos}")