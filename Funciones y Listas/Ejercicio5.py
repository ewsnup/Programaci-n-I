from listas_personas import nombres, edades


def persona_menor_edad(nombre, edades):
    persona_menor = []
    edad = 0
    for i in range(len(edades)):
        if edades[i] < 25:
            persona_menor.append((nombres[i], edades[i]))
    return persona_menor

persona_menor = persona_menor_edad(nombres, edades)

for i in persona_menor:
    print(f"Nombre: {i[0]}, Edad: {i[1]}")