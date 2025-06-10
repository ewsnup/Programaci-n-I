def inicializar_lista()->list:
    numeros = [0] * 10

    for i in range(len(numeros)):
        posicion = int(input("Ingrese la posicion de la lista: "))
        valor = int(input("Ingrese el valor: "))
        numeros[i] = valor


    return numeros

print(inicializar_lista())