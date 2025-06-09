'''
Se tiene una lista de diccionarios donde cada uno representa una película con título, año y puntaje. 
Escribe una función procesar_peliculas que reciba esa lista y una función como parámetro. 
Luego, implementa:

 Una función que devuelva las películas ordenadas por puntaje de mayor a menor.
 Otra función que ordene las películas por año de estreno de menor a mayor.

'''

peliculas = [
{"titulo": "Inception", "año": 2010, "puntaje": 8.8},
{"titulo": "The Matrix", "año": 1999, "puntaje": 8.7},
{"titulo": "Interstellar", "año": 2014, "puntaje": 8.6},
{"titulo": "Avatar", "año": 2009, "puntaje": 7.8},
{"titulo": "The Batman", "año": 2022, "puntaje": 7.9}
]

def procesar_peliculas(peliculas, operacion):
    return operacion(peliculas)

def ordenado_may_men(peliculas):

    for i in range(len(peliculas)-1):
        for j in range(i+1,len(peliculas)):
            if (peliculas[i]["puntaje"] < peliculas[j]["puntaje"]):
                aux = peliculas[i]["puntaje"]
                peliculas[i]["puntaje"] = peliculas[j]["puntaje"]
                peliculas[j]["puntaje"] = aux
    return peliculas
    
def ordenado_año_estreno(peliculas):
    for i in range(len(peliculas)-1):
        for j in range(i+1,len(peliculas)):
            if (peliculas[i]["año"] > peliculas[j]["año"]):
                aux = peliculas[i]["año"]
                peliculas[i]["año"] = peliculas[j]["año"]
                peliculas[j]["año"] = aux
    return peliculas
    
peliculas_ordenadas_año = procesar_peliculas(peliculas, ordenado_año_estreno)
print("Año de estreno de cada película:")
for pelicula in peliculas_ordenadas_año:
    print(f"{pelicula['titulo']}: {pelicula['año']}")

print("")

print("Puntaje de cada película:")
peliculas_ordenadas = procesar_peliculas(peliculas, ordenado_may_men)
for pelicula in peliculas_ordenadas:
    print(f"{pelicula['titulo']}: {pelicula['puntaje']}")