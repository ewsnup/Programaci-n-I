def sumar_digitos(num:int)->int:
    '''
    Si el numero es de un digito se devuelve ese numero
    De lo contrario se saca el el ultimo digito del numero
    Luego elimina el ultimo digito diviendo el numero entero por 10
    '''
    if num < 10:
        return num
    return (num % 10) + sumar_digitos(num // 10)

numero = int(input("Ingrese un numero: "))
print(f"La suma de los digitos de {numero} es de: {sumar_digitos(numero)}")