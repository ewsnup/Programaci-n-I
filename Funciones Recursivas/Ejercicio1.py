def sumar_naturales(num:int)->int:
    '''
    la funcion se llama a sí misma con el numero ingresado
    restandole 1 hasta llegar a 0 
    '''
    if num == 0:
        return 0
    else:
        return num + sumar_naturales (num - 1)
    

num1 = int(input("Ingrese un numero: "))
print(f"La suma de {num1} es de: {sumar_naturales(num1)}")