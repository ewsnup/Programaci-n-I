def imprimir_tabla_multiplicar(num:int, inicio:int, fin:int):
    return

numero = int(input("Ingrese un numero: "))
inicio = int(input("Ingrese desde qué numero quiere multiplicar: "))
fin = int(input("Ingrese hasta qué numero quiere multiplicar: "))


for i in range(inicio, fin + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

imprimir_tabla_multiplicar(numero, inicio, fin)