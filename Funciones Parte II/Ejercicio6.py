def calcular_potencia(base:int, exponente:int)->int:
    resultado = base ** exponente
    return resultado

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = calcular_potencia(base, exponente)
print(f"La potencia de {base} es: ", resultado)