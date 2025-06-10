emp_masc = 0
resp_a = 0
resp_b = 0
emp_fem = 0
ia = 0
rv = 0
iot = 0
emp_enc = 10
may_edad = 0
nom_may = ""
tec_may = ""

for i in range(emp_enc):
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad (18 >): "))
    while (edad < 18):
        edad = int(input("Error. Ingrese su edad (18 >): "))
        
    genero = input("Ingrese su género (Fem - Masc - Otro): ")
    while genero != "Fem" and genero != "Masc" and genero != "Otro":
        genero = input("Error. Ingrese su género (Fem - Masc - Otro): ")
    if genero == "Masc":
        emp_masc += 1

    tecno = input("Ingrese la tecnologia por la que vota (IA, RV/RA, IOT): ")
    while tecno != "IA" and tecno != "RV/RA" and tecno != "IOT":
        tecno = input("Error. Ingrese la tecnologia por la que vota (IA, RV/RA, IOT): ")
    if tecno == "IA":
        ia += 1
    elif tecno == "RV/RA":
        rv += 1
    else:
        tecno == "IOT"
        iot += 1

    if genero == "Masc":
        emp_masc += 1

        if edad > may_edad:
            may_edad = edad
            nom_may = nombre
            tec_may = tecno

        if 25 <= edad <= 50 and (tecno == "IA" or tecno == "IOT"):
            resp_a += 1

    elif genero != "Fem" or (33 > edad <= 40) and (tecno == "IOT" or tecno == "RV/RA"):
        resp_b += 1
    

print(f"La cantidad de empleados masculinos entre 25 y 50 años que votaron por IOT o IA fueron: {resp_a}")
print(f"El porcentaje de empleados entre 33 y 40 años que no votaron por IA fueron: ", (resp_b / emp_enc) * 100)
print(f"El empleado masculino de mayor edad es: {nom_may}, y votó por la tecnología: {tec_may}")