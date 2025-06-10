def calcular_area_circulo(radio:int)->int:
    area = valor_radio * pi
    return area

radio = int(input("Ingresa el radio del circulo: "))
valor_radio = radio ** 2
pi = 3.1416

area = calcular_area_circulo(radio)
print ("El resultado del Area es: ", area)