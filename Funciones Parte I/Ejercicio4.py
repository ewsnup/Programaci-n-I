def validar_numero(num, desde, hasta):
    """""
    esta funcion valida el numero ingresado y los otros dos numeros ingresados (desde, hasta)
    si el numero esta dentro del rango devuelve un print con el numero ingresado y los rangos
    si el numero no esta dentro del rango devuelve lo mismo pero con un mensaje negativo
    """""
    if desde <= num <= hasta:
        print(f"El número {num} está dentro del rango [{desde}, {hasta}].")
    else:
        print(f"El número {num} no está dentro del rango [{desde}, {hasta}].")

def numero_ingresado():
    """""
    esta funcion esta para ingresar el numero que se va a validar en la funcion anterior
    se ingresa el numero y lo devuelve
    """""
    num = int(input("Ingrese un número: "))
    return num

desde = int(input("Ingrese el límite inferior del rango (desde): "))
hasta = int(input("Ingrese el límite superior del rango (hasta): "))

numero = numero_ingresado()
validar_numero(numero, desde, hasta)