
from estudiantes import *
from funciones_diccionario import *


seguir = True
while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1- Listar alumnos ordenados por apellido y nombre")
    print("2- Obtener promedio de notas por estudiante")
    print("3- Listar estudiantes de Ingeniería en Informática")
    print("4- Obtener promedio de edad de los estudiantes")
    print("5- Informar alumno con mayor promedio")
    print("6- Listar miembros del Club de Informática")
    print("7- Listar alumnos más jóvenes con sus programas")
    print("8- Salir")
        
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        print("")
        estudiantes_ordenados = ordenar_estudiantes_burbuja(estudiantes)
        for estudiante in estudiantes_ordenados:
            print(f"Legajo: {estudiante['legajo']}, Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Edad: {estudiante['edad']}")
    elif opcion == "2": 
        print("")
        promedio_notas = sacar_promedio(estudiantes)
        for resultado in promedio_notas:
            print(f"{resultado['nombre']} {resultado['apellido']}: {resultado['promedio']:.2f}")
    elif opcion == "3":
        print("")
        resultado = ingenieria_informatica(estudiantes)
        for estudiante in resultado:
            print(f"Legajo: {estudiante['legajo']}, Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Edad: {estudiante['edad']}")
    elif opcion == "4":
        print("")
        promedio = promedio_edad(estudiantes)
        print(f"\nPromedio de edad de los estudiantes: {promedio['promedio_edad']} años")
        for estudiante in promedio["estudiantes"]:
            print(f"Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}")
    elif opcion == "5":
        print("")
        resultado = alumno_max_promedio(estudiantes)
        print(f"\nEl alumno con mayor promedio es: {resultado['nombre']} {resultado['apellido']}")
        print(f"Promedio: {resultado['promedio']:.2f}")
    elif opcion == "6":
        print("")
        promedio_club = listar_miembros_informatica(estudiantes)
        for resultado in promedio_club:
            print(f"{resultado['nombre']} {resultado['apellido']}: {resultado['promedio']:.2f}")
    elif opcion == "7":
        print("")
        alumnos_jovenes = listar_alumnos_jovenes(estudiantes)
        for estudiante in alumnos_jovenes:
            print(f"Legajo: {estudiante['legajo']}, Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Programa: {estudiante['programa']}")
    elif opcion == "8":
        seguir = False
        print("\nSaliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
    if not continuar_programa():
        print("\nSaliendo del programa...")
        break
    
