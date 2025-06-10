def determinar_par(num:int)->bool:
    resultado = False
    if num % 2 == 0:
        resultado = True
    return resultado

numero = int(input("Ingrese un numero: "))
respuesta = determinar_par(numero)
if determinar_par(numero):
    print(f"{numero} Es par")
else:
    print(f"{numero} No es par")