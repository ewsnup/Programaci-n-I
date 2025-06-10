def pedir_nombres():
    nombres = [None] * 10

    for i in range(10):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        nombres[i] = nombre

    return nombres

lista_nombres = pedir_nombres()

print(f"Los nombres ingresados son:")
print(lista_nombres)
