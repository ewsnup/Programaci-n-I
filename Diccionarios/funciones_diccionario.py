from estudiantes import *

def continuar_programa()->bool:
    respuesta = input("\n¿Desea continuar usando el programa? (s/n): ").upper()
    return respuesta == "S"

#1 Listar los alumnos por orden ascendente de apellido, si se repite, ordenar por nombre. Mostrar legajo, nombre, apellido y edad.

def ordenar_estudiantes_burbuja(estudiante:dict)->dict:
    
    for i in range(len(estudiantes)-1):
        for j in range(i+1,len(estudiantes)):
            if estudiantes[i]["apellido"] > estudiantes[j]["apellido"]:
                estudiantes[i], estudiantes[j] = estudiantes[j], estudiantes[i]
                
            elif estudiantes[i]["apellido"] == estudiantes[j]["apellido"]:

                if estudiantes[i]["nombre"] > estudiantes[j]["nombre"]:
                    estudiantes[i], estudiantes[j] = estudiantes[j], estudiantes[i]

    return estudiantes

#2 Obtener el promedio de notas para cada estudiante.

def sacar_promedio(estudiantes:dict)->list:
    promedios_estudiantes = []
    
    for estudiante in estudiantes:
        suma_notas = 0
        for nota in estudiante["notas"]:
            suma_notas += nota
        promedio_individual = suma_notas / len(estudiante["notas"])
        promedios_estudiantes.append({
            "nombre": estudiante["nombre"],
            "apellido": estudiante["apellido"],
            "promedio": promedio_individual
        })
    
    return promedios_estudiantes


#3 Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de “Ingenieria en Informatica”

def ingenieria_informatica(estudiantes:dict)->list:
    lista = []
    for estudiante in estudiantes:
        if estudiante["programa"]["nombre"] == "Ingenieria en Informatica":
            lista.append({
                "legajo": estudiante["legajo"],
                "nombre": estudiante["nombre"],
                "apellido": estudiante["apellido"],
                "edad": estudiante["edad"]
            })

    return lista

#4 Obtener un promedio de edad de los estudiantes. Mostrar nombre y apellido.

def promedio_edad(estudiantes:dict)->dict:
    suma_edades = 0
    lista_estudiantes = []
    
    for estudiante in estudiantes:
        suma_edades += estudiante["edad"]
        lista_estudiantes.append({
            "nombre": estudiante["nombre"],
            "apellido": estudiante["apellido"]
        })
    
    promedio = suma_edades / len(estudiantes)
    
    return {
        "promedio_edad": (promedio),
        "estudiantes": lista_estudiantes
    }

#5 Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido.

def alumno_max_promedio(estudiantes:dict)->list:
    mejor_alumno = None
    mejor_promedio = 0
    
    for estudiante in estudiantes:
        suma_notas = 0
        for nota in estudiante["notas"]:
            suma_notas += nota
        promedio_actual = suma_notas / len(estudiante["notas"])
        
        if promedio_actual > mejor_promedio:
            mejor_promedio = promedio_actual
            mejor_alumno = {
                "nombre": estudiante["nombre"],
                "apellido": estudiante["apellido"],
                "promedio": promedio_actual
            }
    
    return mejor_alumno

#6 Listar nombre y apellido de los alumnos que forman el grupo “Club de Informática” con sus respectivos promedios

def listar_miembros_informatica(estudiantes:dict)->list:
    miembros_informatica = []
    
    for estudiante in estudiantes:
        if "grupos" in estudiante:
            for grupo in estudiante["grupos"]:
                if grupo["nombre"] == "Club de Informatica":
                    total_notas = 0
                    cantidad_notas = 0
                    for nota in estudiante["notas"]:
                        total_notas += nota
                        cantidad_notas += 1
                    
                    promedio = total_notas / cantidad_notas
                    
                    miembros_informatica.append({
                        "nombre": estudiante["nombre"],
                        "apellido": estudiante["apellido"],
                        "promedio": promedio
                    })
                    break
    
    return miembros_informatica

#7 Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes

def listar_alumnos_jovenes(estudiantes:dict)->list:
    alumnos_jovenes = []

    for estudiante in estudiantes:
        if estudiante["edad"] <= 25:
            alumnos_jovenes.append({
                "legajo": estudiante["legajo"],
                "nombre": estudiante["nombre"],
                "apellido": estudiante["apellido"],
                "programa": estudiante["programa"]["nombre"]
            })
    
    return alumnos_jovenes