# Algoritmo de ordenamiento: Insertion Sort por nombre
def insertion_sort_nombre(lista):
    """Ordena la lista de clientes por nombre usando Insertion Sort"""
    lista_copia = lista.copy()
    comparaciones = 0
    
    for i in range(1, len(lista_copia)):
        key = lista_copia[i]
        j = i - 1
        
        # Mover elementos que son mayores que key hacia adelante
        while j >= 0:
            comparaciones += 1
            if lista_copia[j][0] > key[0]:  # Comparar por nombre (índice 0)
                lista_copia[j + 1] = lista_copia[j]
                j -= 1
            else:
                break
        
        lista_copia[j + 1] = key
    
    print(f"\n--- Insertion Sort por nombre ---")
    print(f"Comparaciones realizadas: {comparaciones}")
    return lista_copia

# Algoritmo de ordenamiento: Selection Sort por saldo
def selection_sort_saldo(lista):
    """Ordena la lista de clientes por saldo usando Selection Sort"""
    lista_copia = lista.copy()
    comparaciones = 0
    
    for i in range(len(lista_copia)):
        min_idx = i
        
        for j in range(i + 1, len(lista_copia)):
            comparaciones += 1
            if lista_copia[j][1] < lista_copia[min_idx][1]:  # Comparar por saldo (índice 1)
                min_idx = j
        
        # Intercambiar elementos
        lista_copia[i], lista_copia[min_idx] = lista_copia[min_idx], lista_copia[i]
    
    print(f"\n--- Selection Sort por saldo ---")
    print(f"Comparaciones realizadas: {comparaciones}")
    return lista_copia

# Búsqueda binaria por nombre
def busqueda_binaria_nombre(lista_ordenada, nombre_buscado):
    """Realiza búsqueda binaria por nombre en lista ordenada"""
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    comparaciones = 0
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        
        if lista_ordenada[medio][0] == nombre_buscado:
            return medio, comparaciones, True
        elif lista_ordenada[medio][0] < nombre_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1, comparaciones, False

# Búsqueda lineal (para comparación)
def busqueda_lineal_nombre(lista, nombre_buscado):
    """Realiza búsqueda lineal por nombre"""
    comparaciones = 0
    
    for i, cliente in enumerate(lista):
        comparaciones += 1
        if cliente[0] == nombre_buscado:
            return i, comparaciones, True
    
    return -1, comparaciones, False