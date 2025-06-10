def buscar_numero(nume:int, lista_numeros:list)->bool:
    for i in range(len(lista_numeros)):
        nume == False
        if i == nume:
            return True
        
lista_numeros = [20, 57, 37, 57, 24, 59, 51, 40, 29, 49, 60, 26, 52, 58, 49, 56, 20, 60, 35, 22, 31, 47, 44, 29, 60, 36, 48, 27, 48, 50, 29, 26, 47, 47, 42, 53, 38, 50, 52, 57, 35, 53, 47, 21, 28, 55, 20, 58, 25, 29]
nume = int(input("Ingrese el numero qe desee buscar: "))

numero_especifico = buscar_numero(nume, lista_numeros)
print(numero_especifico)