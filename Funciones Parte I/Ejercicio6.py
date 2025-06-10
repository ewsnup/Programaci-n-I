def numero1(num:int)->bool:
    resultado = False
    if num < 10 or num > 100:
        resultado = True
    #else:
     #   resultado = False
    return resultado

def realizar_descuento(valor:int)->int:
    descuento = valor * 0.05
    return valor - descuento

numero = int(input("Ingrese un numero: "))
respuesta = numero1(numero)
if numero1(numero):
    print(f"{numero} no está dentro de los parametros")
else:
    print(f"{numero} está dentro de los parametros")
    resultado = realizar_descuento(numero)
    print(f"El valor con el 5% de descuento es: {resultado}")