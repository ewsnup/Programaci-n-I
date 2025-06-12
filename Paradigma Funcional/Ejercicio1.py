def procesar_productos(productos, operacion):
    """
    Función principal que procesa una lista de productos según la operación especificada.
    
    Parametros:
        productos: Lista de diccionarios con información de productos.
        operacion: Función que define qué operación realizar sobre los productos.
    
    Returns:
        Resultado de aplicar la operación a los productos.
    """
    return operacion(productos)

def filtrar_por_categoria(categoria):
    """
    Devuelve una función que filtra productos por categoría.
    
    Parametro:
        categoria: Categoría por la cual filtrar los productos.
    
    Returns:
        Función que realiza el filtrado.
    """
    def filtrador(productos):
        resultado = []
        for producto in productos:
            if producto["categoria"] == categoria:
                resultado.append(producto)
        return resultado
    return filtrador

def calcular_precio_promedio(productos):
    """
    Calcula el precio promedio de todos los productos.
    
    Parametro:
        productos: Lista de productos.
    
    Returns:
        Precio promedio como float.
    """
    total = sum(producto["precio"] for producto in productos)
    return total / len(productos)


productos = [
        {"nombre": "Laptop", "precio": 1200, "categoria": "tecnología"},
        {"nombre": "Silla", "precio": 150, "categoria": "hogar"},
        {"nombre": "Smartphone", "precio": 800, "categoria": "tecnología"},
        {"nombre": "Mesa", "precio": 300, "categoria": "hogar"},
        {"nombre": "Auriculares", "precio": 200, "categoria": "tecnología"}
    ]
    

print("Productos de tecnología:")
for producto in procesar_productos(productos, filtrar_por_categoria("tecnología")): 
    print(f"- {producto['nombre']}: ${producto['precio']}")

print("\nPrecio promedio:", procesar_productos(productos, calcular_precio_promedio))
