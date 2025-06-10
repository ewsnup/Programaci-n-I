from lista_personas import *
from Biblioteca import *

seguir = True
while True:
    print("\nBienvenido al menú de opciones:")
    print("")
    print("1. Datos de los usuarios de México")
    print("2. Nombre, Email y Teléfono de los usuarios de Brasil")
    print("3. Datos de los usuarios más jóvenes")
    print("4. Datos de los usuarios mayores en Brasil")
    print("5. Promedio de edad de los usuarios")
    print("6. Datos de los usuarios de México y Brasil con código postal > 8000")
    print("7. Nombre, Email y Teléfono de los usuarios italianos mayores a 40 años")
    print("8. Datos de los usuarios de México ordenados por nombre") 
    print("9. Datos de los usuarios más jovenes ordenados por edad/por nombre.")
    print("10. Datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
    print("11. Salir")

    opcion = input("\nSeleccione una opción: ")

    match opcion:
        case "1":
            usuarios_mexico = obtener_usuarios_mexico(nombres, telefonos, mails, address, postalZip, region, country)
            for usuario in usuarios_mexico:
                print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")
        case "2":
            usuarios_brasil = obtener_usuarios_brasil(nombres, mails, telefonos)
            for usuario in usuarios_brasil:
                print(f"Nombre: {usuario[0]}, Email: {usuario[1]}, Teléfono: {usuario[2]}")
        case "3":
            usuarios_jovenes = obtener_usuarios_jovenes(nombres, telefonos, mails, address, postalZip, region, country)
            for usuario in usuarios_jovenes:
                print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")
        case "4":
            usuarios_mayores_br = obtener_usuarios_mayores_br(nombres, telefonos, mails, address, postalZip, region, country)
            for usuario in usuarios_mayores_br:
                print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")
        case "5":
            promedio = obtener_promedio_edad(edades)
            print(f"El promedio de edad es: {promedio}")
        case "6":
            usuarios_postal = usuarios_mex_br_postal(nombres, telefonos, mails, address, postalZip, region, country)
            for usuario in usuarios_postal:
                print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")
        case "7":
            usuarios_italianos = italianos_mayores_40(nombres, mails, telefonos)
            for usuario in usuarios_italianos:
                print(f"Nombre: {usuario[0]}, Email: {usuario[1]}, Telefono: {usuario[2]}")
        case "8":
            ordenados = usuarios_ordenados()
            for usuario in ordenados:
                print(f"Nombre: {usuario[0]}, Teléfono: {usuario[1]}, Email: {usuario[2]}, Dirección: {usuario[3]}, Código Postal: {usuario[4]}, Región: {usuario[5]}")
        case "9":
            datos_ordenados = ordenar_datos(obtener_usuarios_jovenes(nombres, telefonos, mails, address, postalZip, region, country))
            for i in datos_ordenados:
                print(i)
        case "10":
            datos_ordenados = ordenar_datos(usuarios_mex_br_postal(nombres, telefonos, mails, address, postalZip, region, edades))
            for i in datos_ordenados:
                print(i)
        case "11":
            op = input("¿Está seguro de que desea salir del programa? (S/N): ").upper()
            if op == "N":
                seguir = True
            else:
                seguir = False
                print("\nSaliendo del programa...")
                break
        case _:
            print("Error.")
