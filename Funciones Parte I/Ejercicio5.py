def restar1(num1:int, num2:int)->int:
    resultado = num1 - num2
    return resultado

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))

respuesta = restar1(numero1, numero2)
print("El resultado de la resta es: ", respuesta)

def restar2()->int:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    resultado = num1 - num2
    print("El resultado de la resta es: ", resultado)

restar2()

def restar3()->int:
    nume1 = int(input("Ingrese un numero: "))
    nume2 = int(input("Ingrese un numero: "))
    resultado = nume1 - nume2
    return resultado

respuesta = restar3()
print("EL resultado de la resta es de: ", respuesta)
    
def restar4(num1:int, num2:int):
    resultado = num1 - num2
    print("El resultado de la resta es de: ", resultado)

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))
restar4(numero1, numero2)