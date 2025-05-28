# Sistema Inteligente de Gestión de Clientes

# Parte 1: Datos iniciales
clientes = [
    ("Carlos", 100.0),
    ("Ana", 50.5),
    ("Pedro", 250.75),
    ("Maria", 75.25),
    ("Juan", 300.0),
    ("Sofia", 125.80),
    ("Luis", 180.45),
    ("Carmen", 95.60),
    ("Diego", 220.30),
    ("Elena", 65.90),
    ("Roberto", 400.15),
    ("Lucia", 85.25)
]

print("=== SISTEMA DE GESTIÓN DE CLIENTES ===")
print(f"Base de datos inicial con {len(clientes)} clientes:")
for i, cliente in enumerate(clientes, 1):
    print(f"{i:2d}. {cliente[0]:<10} - Saldo: ${cliente[1]:>7.2f}")

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

# Función para agregar nuevo cliente
def agregar_cliente(lista, nombre, saldo):
    """Agrega un nuevo cliente a la lista"""
    try:
        saldo_float = float(saldo)
        lista.append((nombre, saldo_float))
        print(f"Cliente '{nombre}' agregado exitosamente con saldo ${saldo_float:.2f}")
        return True
    except ValueError:
        print("Error: El saldo debe ser un número válido")
        return False

# Demostración del sistema
print("\n" + "="*50)
print("DEMOSTRACIÓN DEL SISTEMA")
print("="*50)

# 1. Ordenamiento por nombre
clientes_por_nombre = insertion_sort_nombre(clientes)
print("\nClientes ordenados por nombre:")
for i, cliente in enumerate(clientes_por_nombre, 1):
    print(f"{i:2d}. {cliente[0]:<10} - Saldo: ${cliente[1]:>7.2f}")

# 2. Ordenamiento por saldo
clientes_por_saldo = selection_sort_saldo(clientes)
print("\nClientes ordenados por saldo (menor a mayor):")
for i, cliente in enumerate(clientes_por_saldo, 1):
    print(f"{i:2d}. {cliente[0]:<10} - Saldo: ${cliente[1]:>7.2f}")

# 3. Búsqueda de clientes
print("\n" + "="*50)
print("BÚSQUEDA DE CLIENTES")
print("="*50)

# Ejemplos de búsqueda
nombres_a_buscar = ["Maria", "Carlos", "Alejandro"]

for nombre in nombres_a_buscar:
    print(f"\n--- Buscando cliente: '{nombre}' ---")
    
    # Búsqueda binaria (requiere lista ordenada)
    posicion_bin, comp_bin, encontrado_bin = busqueda_binaria_nombre(clientes_por_nombre, nombre)
    
    # Búsqueda lineal (en lista original)
    posicion_lin, comp_lin, encontrado_lin = busqueda_lineal_nombre(clientes, nombre)
    
    if encontrado_bin:
        cliente_encontrado = clientes_por_nombre[posicion_bin]
        print(f"✅ Cliente encontrado!")
        print(f"   Nombre: {cliente_encontrado[0]}")
        print(f"   Saldo: ${cliente_encontrado[1]:.2f}")
        print(f"   Posición en lista ordenada: {posicion_bin + 1}")
    else:
        print(f"❌ Cliente '{nombre}' no encontrado")
    
    print(f"   Búsqueda binaria: {comp_bin} comparaciones")
    print(f"   Búsqueda lineal: {comp_lin} comparaciones")
    print(f"   Eficiencia: La búsqueda binaria fue {comp_lin/comp_bin:.1f}x más eficiente" if comp_bin > 0 else "")

# 4. Funcionalidad extra: Agregar nuevo cliente
print("\n" + "="*50)
print("AGREGAR NUEVO CLIENTE")
print("="*50)

# Simulación de agregar un cliente
print("Agregando nuevo cliente...")
if agregar_cliente(clientes, "Fernando", "150.75"):
    print(f"Total de clientes ahora: {len(clientes)}")
    print("Último cliente agregado:", clientes[-1])

# Opción interactiva (comentada para ejecución automática)
"""
# Sección interactiva para el usuario
print("\n" + "="*50)
print("MODO INTERACTIVO")
print("="*50)

while True:
    print("\nOpciones:")
    print("1. Buscar cliente")
    print("2. Agregar cliente")
    print("3. Ver lista completa")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ").strip()
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente a buscar: ").strip()
        
        usar_binaria = input("¿Usar búsqueda binaria? (s/n): ").strip().lower() == 's'
        
        if usar_binaria:
            clientes_ordenados = insertion_sort_nombre(clientes)
            pos, comp, encontrado = busqueda_binaria_nombre(clientes_ordenados, nombre)
            tipo_busqueda = "binaria"
        else:
            pos, comp, encontrado = busqueda_lineal_nombre(clientes, nombre)
            tipo_busqueda = "lineal"
        
        if encontrado:
            if usar_binaria:
                cliente = clientes_ordenados[pos]
            else:
                cliente = clientes[pos]
            print(f"✅ Cliente encontrado: {cliente[0]} - ${cliente[1]:.2f}")
            print(f"Posición: {pos + 1}, Comparaciones: {comp}")
        else:
            print(f"❌ Cliente no encontrado. Comparaciones: {comp}")
    
    elif opcion == "2":
        nombre = input("Nombre del nuevo cliente: ").strip()
        saldo = input("Saldo del cliente: ").strip()
        agregar_cliente(clientes, nombre, saldo)
    
    elif opcion == "3":
        print(f"\nLista actual de {len(clientes)} clientes:")
        for i, cliente in enumerate(clientes, 1):
            print(f"{i:2d}. {cliente[0]:<12} - ${cliente[1]:>7.2f}")
    
    elif opcion == "4":
        print("¡Gracias por usar el sistema!")
        break
    
    else:
        print("Opción no válida. Intente de nuevo.")
"""

print("\n" + "="*50)
print("SISTEMA COMPLETADO")
print("="*50)