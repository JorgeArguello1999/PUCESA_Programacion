"""
Sistema de Búsqueda de Productos para una Tienda Virtual

Este programa implementa dos algoritmos de búsqueda:
1. Búsqueda Lineal: Examina cada elemento secuencialmente hasta encontrar el objetivo.
   - Ventaja: Funciona en listas ordenadas y desordenadas.
   - Desventaja: Tiene complejidad O(n), ineficiente para listas grandes.

2. Búsqueda Binaria: Divide la lista por la mitad en cada paso para reducir el espacio de búsqueda.
   - Ventaja: Tiene complejidad O(log n), muy eficiente para listas grandes.
   - Desventaja: Requiere que la lista esté ordenada.
"""

def busqueda_lineal(lista, objetivo):
    """
    Realiza una búsqueda lineal en la lista para encontrar el objetivo.
    
    Args:
        lista: Lista de elementos donde buscar
        objetivo: Elemento que se busca
        
    Returns:
        Tupla (posición, comparaciones) si se encuentra el elemento,
        o (-1, comparaciones) si no se encuentra
    """
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i].lower() == objetivo.lower():  # Comparación insensible a mayúsculas/minúsculas
            return i, comparaciones
    return -1, comparaciones

def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en la lista para encontrar el objetivo.
    La lista debe estar ordenada.
    
    Args:
        lista: Lista ordenada de elementos donde buscar
        objetivo: Elemento que se busca
        
    Returns:
        Tupla (posición, comparaciones) si se encuentra el elemento,
        o (-1, comparaciones) si no se encuentra
    """
    comparaciones = 0
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        comparaciones += 1
        
        # Comparación insensible a mayúsculas/minúsculas
        if lista[medio].lower() == objetivo.lower():
            return medio, comparaciones
        elif lista[medio].lower() < objetivo.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return -1, comparaciones

def mostrar_resultado(nombre, posicion, comparaciones):
    """Muestra el resultado de la búsqueda de manera formateada"""
    if posicion != -1:
        print(f"✅ '{nombre}' encontrado en la posición {posicion}")
    else:
        print(f"❌ '{nombre}' no fue encontrado")
    print(f"   Se realizaron {comparaciones} comparaciones")

def main():
    # Lista de productos (mínimo 20)
    productos = [
        "Smartphone Samsung Galaxy", 
        "Laptop HP Pavilion", 
        "Audifonos Bluetooth Sony",
        "Monitor LG UltraWide",
        "Teclado mecánico Logitech",
        "Mouse inalámbrico Microsoft",
        "Tablet Apple iPad",
        "Impresora Canon Pixma",
        "Disco duro externo Seagate",
        "Smartwatch Fitbit Versa",
        "Parlante Bluetooth JBL",
        "Cámara digital Nikon",
        "Router WiFi TP-Link",
        "Batería externa Anker",
        "Smart TV Samsung",
        "Consola PlayStation 5",
        "Cafetera Nespresso",
        "Licuadora Oster",
        "Aspiradora robot Roomba",
        "Cargador inalámbrico Belkin",
        "Micrófono Blue Yeti",
        "Reproductor Amazon Fire Stick",
        "Audífonos AirPods Pro"
    ]
    
    # Crear una copia ordenada para la búsqueda binaria
    productos_ordenados = sorted(productos)
    
    # Para almacenar el historial de búsquedas
    historial = []
    
    print("=== 🔍 SISTEMA DE BÚSQUEDA DE PRODUCTOS ===")
    print(f"Catálogo: {len(productos)} productos disponibles\n")
    
    continuar = True
    while continuar:
        # Solicitar producto a buscar
        busqueda = input("\nIngrese el nombre del producto a buscar (o presione Enter para salir): ").strip()
        
        # Validar si está vacío
        if not busqueda:
            print("Búsqueda vacía. ¿Desea salir?")
            respuesta = input("¿Salir del programa? (s/n): ").lower()
            if respuesta == 's' or respuesta == 'si':
                continuar = False
            continue
        
        print("\n--- Resultados de la búsqueda ---")
        
        # Realizar búsqueda lineal
        pos_lineal, comp_lineal = busqueda_lineal(productos, busqueda)
        print("🔹 Búsqueda Lineal:")
        mostrar_resultado(busqueda, pos_lineal, comp_lineal)
        
        # Realizar búsqueda binaria
        pos_binaria, comp_binaria = busqueda_binaria(productos_ordenados, busqueda)
        print("\n🔹 Búsqueda Binaria:")
        # Si encontramos el producto en la lista ordenada, necesitamos mostrar el nombre correcto
        nombre_encontrado = productos_ordenados[pos_binaria] if pos_binaria != -1 else busqueda
        mostrar_resultado(nombre_encontrado, pos_binaria, comp_binaria)
        
        # Guardar en el historial
        historial.append({
            'producto': busqueda,
            'encontrado': pos_lineal != -1 or pos_binaria != -1,
            'comp_lineal': comp_lineal,
            'comp_binaria': comp_binaria
        })
        
        print("\n¿Desea buscar otro producto?")
        respuesta = input("Continuar (s/n): ").lower()
        if respuesta != 's' and respuesta != 'si':
            continuar = False
    
    # Mostrar resumen de búsquedas
    if historial:
        print("\n\n=== 📊 RESUMEN DE BÚSQUEDAS ===")
        print(f"Total de búsquedas realizadas: {len(historial)}")
        
        encontrados = sum(1 for item in historial if item['encontrado'])
        print(f"Productos encontrados: {encontrados}")
        print(f"Productos no encontrados: {len(historial) - encontrados}")
        
        prom_lineal = sum(item['comp_lineal'] for item in historial) / len(historial)
        prom_binaria = sum(item['comp_binaria'] for item in historial) / len(historial)
        print(f"\nPromedio de comparaciones:")
        print(f"- Búsqueda Lineal: {prom_lineal:.2f}")
        print(f"- Búsqueda Binaria: {prom_binaria:.2f}")
        
        print("\nListado de productos buscados:")
        for i, item in enumerate(historial, 1):
            estado = "✅ Encontrado" if item['encontrado'] else "❌ No encontrado"
            print(f"{i}. '{item['producto']}' - {estado} (Lineal: {item['comp_lineal']} comp., Binaria: {item['comp_binaria']} comp.)")
    
    print("\n¡Gracias por usar el Sistema de Búsqueda de Productos!")

if __name__ == "__main__":
    main()