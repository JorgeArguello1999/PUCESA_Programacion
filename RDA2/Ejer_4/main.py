# Sistema Inteligente de Gestión de Clientes
from func import insertion_sort_nombre, selection_sort_saldo, busqueda_binaria_nombre, busqueda_lineal_nombre

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

print("\n" + "="*50)
print("SISTEMA COMPLETADO")
print("="*50)