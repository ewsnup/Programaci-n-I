def es_primo(numero)->bool:
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un numero: "))
respuesta = es_primo(numero)
if es_primo(numero):
    print("True")
else:
    print("False")