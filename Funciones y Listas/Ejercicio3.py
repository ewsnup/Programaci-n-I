def pedir_numeros()->list:
    lista_numeros = [0] * 10

    for i in range(len(lista_numeros)):
        numero = int(input(f"Ingrese el número {i + 1} dentro del rango 1-100: "))

        if 1 <= numero <= 100:
            lista_numeros[i] = numero
        else:
            print("Número fuera de rango. Se guardará como 0.")

    return lista_numeros

numeros_usuario = pedir_numeros()
print("Los números ingresados son:", numeros_usuario)