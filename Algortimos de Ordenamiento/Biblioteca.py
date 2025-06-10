from lista_personas import *

def obtener_usuarios_mexico(nombres, telefonos, mails, address, postalZip, region, country):
    usuarios_mexico = []
    for i in range(len(country)):
        if country[i] == 'Mexico':
            usuarios_mexico.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))
    return usuarios_mexico


def obtener_usuarios_brasil(nombre, mail, telefono):
    usuarios_brasil = []
    for i in range(len(country)):
        if country[i] == 'Brazil':
            usuarios_brasil.append((nombres[i], mails[i], telefonos[i]))
    return usuarios_brasil

def obtener_usuarios_jovenes(nombres, telefonos, mails, address, postalZip, region, country):
    usuarios_jovenes = []
    for i in range(len(edades)):
        if edades[i] <= 24:
            usuarios_jovenes.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))
    return usuarios_jovenes

def obtener_promedio_edad(edades):
    suma = 0
    if len(edades) == 0:
        return 0
    for i in edades:
        suma += i

    promedio = suma // len(edades)

    return promedio

def obtener_usuarios_mayores_br(nombres, telefonos, mails, address, postalZip, region, country):
    usuarios_mayores_br = []

    for i in range(len(country)):
        if country[i] == 'Brazil' and edades[i] >= 24:
            usuarios_mayores_br.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))

    return usuarios_mayores_br


def usuarios_mex_br_postal(nombres, telefonos, mails, address, postalZip, region, edades):
    usuarios_postal = []
    for i in range(len(postalZip)):
        if postalZip[i] > 8000 and country[i] in ["Mexico", "Brazil"]:
            usuarios_postal.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i]))
    return usuarios_postal

def italianos_mayores_40(nombre, mail, telefono):
    usuarios_italianos = []
    for i in range(len(country)):
        if country[i] == 'Italy' and edades[i] >= 40:
            usuarios_italianos.append((nombres[i], mails[i], telefono[i]))
    return usuarios_italianos



def usuarios_ordenados():
    usuarios_mexico = obtener_usuarios_mexico(nombres, telefonos, mails, address, postalZip, region, country)

    for i in range(len(usuarios_mexico)-1):
        for j in range(i+1,len(usuarios_mexico)):
            if(usuarios_mexico[i] > usuarios_mexico[j]):
                aux = usuarios_mexico[i]
                usuarios_mexico[i] = usuarios_mexico[j]
                usuarios_mexico[j] = aux
    return usuarios_mexico

def ordenar_datos(datos:list)->list:

    for i in range(len(datos)-1):
        for j in range(i+1,len(datos)):
            if (datos[i] > datos[j]):
                aux = datos[i]
                datos[i] = datos[j]
                datos[j] = aux
                
    return datos


def edad_ascendente(edades:list)->list:

    for i in range(len(edades)-1):
        for j in range(i+1,len(edades)):
            if(edades[i] > edades[j]):
                aux = edades[i]
                edades[i] = edades[j]
                edades[j] = aux
    return edades