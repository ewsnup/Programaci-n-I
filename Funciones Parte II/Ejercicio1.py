def calcular_area_rectangulo(base:int, altura:int)->int:
    area = base * altura
    return area

base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))

area = calcular_area_rectangulo(base, altura)
print ("El resultado del Area es: ", area)