'''
Se tiene una lista de diccionarios donde cada diccionario representa un estudiante con su nombre, curso y calificación. 
Escribe una función procesar_estudiantes que reciba esa lista y una función como parámetro. 
Luego, implementa:

 Una función que devuelva solo los estudiantes aprobados (nota mayor o igual a 6.0).
 Otra que calcule el promedio de calificaciones de todos los estudiantes.

'''

estudiantes = [
{"nombre": "Sofía", "curso": "Matemáticas", "calificacion": 7.5},
{"nombre": "Tomás", "curso": "Historia", "calificacion": 5.5},
{"nombre": "Valentina", "curso": "Ciencias", "calificacion": 9.0},
{"nombre": "Lucas", "curso": "Literatura", "calificacion": 4.0},
{"nombre": "Martina", "curso": "Física", "calificacion": 6.8}
]

def procesar_estudiantes(estudiantes, operacion):
    return operacion(estudiantes)

def filtrar_notas(calificacion):
    def filtrador(estudiantes):
        lista = []
        for estudiante in estudiantes:
            if estudiante["calificacion"] >= calificacion:
                lista.append(estudiante)
        return lista 
    return filtrador  

def calcular_promedio_notas(calificacion):
    total = sum(estudiante["calificacion"] for estudiante in estudiantes)
    return total / len(estudiantes)
    
filtro_aprobados = filtrar_notas(6.0)
aprobados = procesar_estudiantes(estudiantes, filtro_aprobados)

print("Estudiantes aprobados:")
for estudiante in aprobados:
    print(f"- {estudiante['nombre']}: {estudiante['calificacion']}")

print("\nCalifición promedio:", procesar_estudiantes(estudiantes, calcular_promedio_notas))