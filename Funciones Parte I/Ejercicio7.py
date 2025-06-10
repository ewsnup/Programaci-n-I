def validar_numero(num: int) -> bool:
    return num < 10 or num > 100

def realizar_operacion(num1: int, num2: int, operacion: str) -> int:
    if operacion == 's':  
        return num1 + num2
    elif operacion == 'r':  
        return num1 - num2

numero1 = int(input("Ingrese el primer número (entre 10 y 100): "))
numero2 = int(input("Ingrese el segundo número (entre 10 y 100): "))

if validar_numero(numero1) or validar_numero(numero2):
    print("Uno o ambos números no están dentro del rango permitido.")
else:
    operacion = input("¿Qué operación desea realizar? (S para sumar, R para restar): ")
    resultado = realizar_operacion(numero1, numero2, operacion)