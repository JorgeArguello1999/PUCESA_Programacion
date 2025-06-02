"""
🧪 Taller Práctico: Visualización y Gestión de Calificaciones

🎯 Objetivo:
Aplicar los conceptos de ordenamiento (Bubble Sort, sorted) y manipulación de listas 
ordenadas (bisect) para gestionar y analizar calificaciones de estudiantes.

📋 Instrucciones del ejercicio:
1. Genera una lista aleatoria de 15 calificaciones finales (entre 0 y 20).
2. Muestra las notas originales.
3. Ordena las calificaciones con Bubble Sort y visualiza el proceso.
4. Ordena las calificaciones usando sorted() con simulación paso a paso.
5. Inserta una nueva calificación usando bisect.insort().
6. Busca si una nota específica existe con bisect_left.
7. Compara y explica cuál enfoque fue más claro y eficiente.
"""

import random
import bisect
import matplotlib.pyplot as plt
import time
from IPython.display import clear_output
import numpy as np

# ============================================================================
# PASO 1: GENERAR LISTA DE NOTAS
# ============================================================================

def generar_notas_aleatorias(cantidad=15, rango_min=0, rango_max=20):
    """Genera una lista de notas aleatorias sin repetidos"""
    notas = random.sample(range(rango_min, rango_max + 1), cantidad)
    return notas

# Generar las notas iniciales
print("=" * 60)
print("📋 GENERACIÓN DE NOTAS ALEATORIAS")
print("=" * 60)

notas_originales = generar_notas_aleatorias()
print(f"📋 Notas originales ({len(notas_originales)} estudiantes):")
print(f"   {notas_originales}")
print(f"📊 Promedio inicial: {sum(notas_originales)/len(notas_originales):.2f}")

# ============================================================================
# PASO 2: IMPLEMENTAR Y VISUALIZAR BUBBLE SORT
# ============================================================================

def bubble_sort_visualizado(lista, delay=0.5):
    """
    Implementa Bubble Sort con visualización en tiempo real
    Complejidad: O(n²) - Menos eficiente pero educativo para ver el proceso
    """
    arr = lista.copy()  # No modificar la lista original
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    
    print("\n" + "=" * 60)
    print("🔄 ORDENAMIENTO CON BUBBLE SORT (VISUALIZADO)")
    print("=" * 60)
    
    # Configurar la visualización
    plt.ion()  # Modo interactivo
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparaciones += 1
            
            # Visualización actual
            ax1.clear()
            ax2.clear()
            
            # Gráfico de barras principal
            colores = ['lightblue'] * len(arr)
            colores[j] = 'red'      # Elemento actual
            colores[j + 1] = 'orange'  # Elemento comparado
            
            bars = ax1.bar(range(len(arr)), arr, color=colores)
            ax1.set_title(f'Bubble Sort - Pasada {i+1}, Comparando posiciones {j} y {j+1}')
            ax1.set_xlabel('Posición')
            ax1.set_ylabel('Calificación')
            ax1.set_ylim(0, 22)
            
            # Añadir valores en las barras
            for idx, (bar, val) in enumerate(zip(bars, arr)):
                ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, 
                        str(val), ha='center', va='bottom')
            
            # Gráfico de estadísticas
            ax2.bar(['Comparaciones', 'Intercambios'], [comparaciones, intercambios], 
                   color=['skyblue', 'lightcoral'])
            ax2.set_title('Estadísticas del Algoritmo')
            ax2.set_ylabel('Cantidad')
            
            # Añadir valores en las barras de estadísticas
            for idx, val in enumerate([comparaciones, intercambios]):
                ax2.text(idx, val + 0.5, str(val), ha='center', va='bottom')
            
            plt.tight_layout()
            plt.pause(delay)
            
            # Realizar intercambio si es necesario
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
                
                # Mostrar el intercambio
                ax1.clear()
                colores = ['lightblue'] * len(arr)
                colores[j] = 'green'      # Intercambiado
                colores[j + 1] = 'green'  # Intercambiado
                
                bars = ax1.bar(range(len(arr)), arr, color=colores)
                ax1.set_title(f'¡Intercambio realizado! Posiciones {j} y {j+1}')
                ax1.set_xlabel('Posición')
                ax1.set_ylabel('Calificación')
                ax1.set_ylim(0, 22)
                
                for idx, (bar, val) in enumerate(zip(bars, arr)):
                    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, 
                            str(val), ha='center', va='bottom')
                
                plt.pause(delay)
    
    # Mostrar resultado final
    ax1.clear()
    ax2.clear()
    
    bars = ax1.bar(range(len(arr)), arr, color='lightgreen')
    ax1.set_title('🎉 Bubble Sort Completado - Lista Ordenada')
    ax1.set_xlabel('Posición')
    ax1.set_ylabel('Calificación')
    ax1.set_ylim(0, 22)
    
    for idx, (bar, val) in enumerate(zip(bars, arr)):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, 
                str(val), ha='center', va='bottom')
    
    # Estadísticas finales
    ax2.bar(['Comparaciones', 'Intercambios'], [comparaciones, intercambios], 
           color=['skyblue', 'lightcoral'])
    ax2.set_title('Estadísticas Finales')
    ax2.set_ylabel('Cantidad')
    
    for idx, val in enumerate([comparaciones, intercambios]):
        ax2.text(idx, val + 0.5, str(val), ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()
    plt.ioff()
    
    print(f"✅ Bubble Sort completado:")
    print(f"   📊 Comparaciones realizadas: {comparaciones}")
    print(f"   🔄 Intercambios realizados: {intercambios}")
    print(f"   📋 Lista ordenada: {arr}")
    
    return arr, comparaciones, intercambios

# Ejecutar Bubble Sort visualizado
notas_bubble_sort, comp_bubble, inter_bubble = bubble_sort_visualizado(notas_originales, delay=0.8)

# ============================================================================
# PASO 3: SIMULAR SORTED() PASO A PASO
# ============================================================================

def sorted_visualizado(lista, delay=0.5):
    """
    Simula visualmente cómo se construye una lista ordenada con sorted()
    En realidad, sorted() usa Timsort (O(n log n)), pero aquí simulamos
    el proceso de construcción paso a paso para fines educativos
    """
    arr_original = lista.copy()
    arr_ordenada = []
    arr_restante = lista.copy()
    
    print("\n" + "=" * 60)
    print("⚡ ORDENAMIENTO CON SORTED() - SIMULACIÓN PASO A PASO")
    print("=" * 60)
    
    plt.ion()
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
    
    pasos = 0
    
    while arr_restante:
        pasos += 1
        # Encontrar el mínimo (simulando parte del proceso de ordenamiento)
        min_val = min(arr_restante)
        min_idx = arr_restante.index(min_val)
        
        # Mover el mínimo a la lista ordenada
        arr_ordenada.append(min_val)
        arr_restante.remove(min_val)
        
        # Visualización
        ax1.clear()
        ax2.clear()
        ax3.clear()
        
        # Lista original (referencia)
        ax1.bar(range(len(arr_original)), arr_original, color='lightgray', alpha=0.5)
        ax1.set_title('Lista Original (Referencia)')
        ax1.set_ylabel('Calificación')
        ax1.set_ylim(0, 22)
        
        # Lista ordenada (en construcción)
        if arr_ordenada:
            bars2 = ax2.bar(range(len(arr_ordenada)), arr_ordenada, color='lightgreen')
            ax2.set_title(f'Lista Ordenada (Paso {pasos}) - Elemento añadido: {min_val}')
            ax2.set_ylabel('Calificación')
            ax2.set_ylim(0, 22)
            
            # Resaltar el último elemento añadido
            if len(bars2) > 0:
                bars2[-1].set_color('green')
            
            for idx, val in enumerate(arr_ordenada):
                ax2.text(idx, val + 0.3, str(val), ha='center', va='bottom')
        
        # Elementos restantes
        if arr_restante:
            bars3 = ax3.bar(range(len(arr_restante)), arr_restante, color='lightcoral')
            ax3.set_title(f'Elementos Restantes ({len(arr_restante)} pendientes)')
            ax3.set_ylabel('Calificación')
            ax3.set_ylim(0, 22)
            
            for idx, val in enumerate(arr_restante):
                ax3.text(idx, val + 0.3, str(val), ha='center', va='bottom')
        else:
            ax3.set_title('🎉 ¡Todos los elementos procesados!')
            ax3.set_ylim(0, 1)
        
        plt.tight_layout()
        plt.pause(delay)
    
    # Resultado final
    ax1.clear()
    ax2.clear()
    ax3.clear()
    
    # Comparación final
    x_pos = np.arange(len(arr_original))
    width = 0.35
    
    ax1.bar(x_pos - width/2, arr_original, width, label='Original', color='lightcoral', alpha=0.7)
    ax1.bar(x_pos + width/2, arr_ordenada, width, label='Ordenada', color='lightgreen', alpha=0.7)
    ax1.set_title('Comparación: Original vs Ordenada')
    ax1.set_ylabel('Calificación')
    ax1.set_xlabel('Posición')
    ax1.legend()
    ax1.set_ylim(0, 22)
    
    # Estadísticas
    ax2.bar(['Elementos Procesados', 'Pasos Realizados'], [len(arr_ordenada), pasos], 
           color=['skyblue', 'orange'])
    ax2.set_title('Estadísticas del Proceso')
    ax2.set_ylabel('Cantidad')
    
    for idx, val in enumerate([len(arr_ordenada), pasos]):
        ax2.text(idx, val + 0.5, str(val), ha='center', va='bottom')
    
    # Información sobre complejidad
    ax3.text(0.5, 0.7, 'Complejidad Real de sorted():', ha='center', va='center', 
             transform=ax3.transAxes, fontsize=14, fontweight='bold')
    ax3.text(0.5, 0.5, 'O(n log n) - Timsort Algorithm', ha='center', va='center', 
             transform=ax3.transAxes, fontsize=12)
    ax3.text(0.5, 0.3, '(Esta simulación es educativa)', ha='center', va='center', 
             transform=ax3.transAxes, fontsize=10, style='italic')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis('off')
    
    plt.tight_layout()
    plt.show()
    plt.ioff()
    
    print(f"✅ Simulación de sorted() completada:")
    print(f"   📊 Pasos realizados: {pasos}")
    print(f"   📋 Lista ordenada: {arr_ordenada}")
    print(f"   ⚡ Complejidad real: O(n log n) con Timsort")
    
    return arr_ordenada, pasos

# Ejecutar simulación de sorted()
notas_sorted, pasos_sorted = sorted_visualizado(notas_originales, delay=0.6)

# ============================================================================
# PASO 4: INSERTAR NUEVA CALIFICACIÓN CON BISECT
# ============================================================================

print("\n" + "=" * 60)
print("➕ INSERCIÓN DE NUEVA CALIFICACIÓN CON BISECT")
print("=" * 60)

# Usar la lista ordenada con sorted() como base
notas_para_bisect = notas_sorted.copy()
nueva_nota = random.randint(0, 20)  # Generar una nueva nota aleatoria

print(f"📋 Lista ordenada actual: {notas_para_bisect}")
print(f"➕ Nueva calificación a insertar: {nueva_nota}")

# Mostrar dónde se insertará
posicion_insercion = bisect.bisect_left(notas_para_bisect, nueva_nota)
print(f"📍 La nueva nota se insertará en la posición: {posicion_insercion}")

# Visualizar antes y después de la inserción
plt.figure(figsize=(12, 6))

# Antes de la inserción
plt.subplot(2, 1, 1)
bars_antes = plt.bar(range(len(notas_para_bisect)), notas_para_bisect, color='lightblue')
plt.axvline(x=posicion_insercion - 0.5, color='red', linestyle='--', 
           label=f'Inserción en pos. {posicion_insercion}')
plt.title(f'Antes de Insertar - Nueva nota: {nueva_nota}')
plt.ylabel('Calificación')
plt.legend()
plt.ylim(0, 22)

for idx, val in enumerate(notas_para_bisect):
    plt.text(idx, val + 0.3, str(val), ha='center', va='bottom')

# Realizar la inserción
bisect.insort(notas_para_bisect, nueva_nota)

# Después de la inserción
plt.subplot(2, 1, 2)
colores_despues = ['lightblue'] * len(notas_para_bisect)
colores_despues[posicion_insercion] = 'lightgreen'  # Resaltar la nueva nota

bars_despues = plt.bar(range(len(notas_para_bisect)), notas_para_bisect, color=colores_despues)
plt.title('Después de Insertar con bisect.insort()')
plt.xlabel('Posición')
plt.ylabel('Calificación')
plt.ylim(0, 22)

for idx, val in enumerate(notas_para_bisect):
    color = 'green' if idx == posicion_insercion else 'black'
    weight = 'bold' if idx == posicion_insercion else 'normal'
    plt.text(idx, val + 0.3, str(val), ha='center', va='bottom', 
             color=color, fontweight=weight)

plt.tight_layout()
plt.show()

print(f"✅ Inserción completada:")
print(f"   📋 Lista después de insertar: {notas_para_bisect}")
print(f"   📊 Nueva cantidad de elementos: {len(notas_para_bisect)}")

# ============================================================================
# PASO 5: BUSCAR CALIFICACIÓN CON BISECT
# ============================================================================

print("\n" + "=" * 60)
print("🔍 BÚSQUEDA DE CALIFICACIÓN CON BISECT")
print("=" * 60)

# Buscar varias notas para demostrar el funcionamiento
notas_a_buscar = [nueva_nota, 15, 25, min(notas_para_bisect), max(notas_para_bisect)]

print(f"📋 Lista actual: {notas_para_bisect}")
print(f"🔍 Notas a buscar: {notas_a_buscar}")
print()

resultados_busqueda = []

for nota_buscar in notas_a_buscar:
    posicion = bisect.bisect_left(notas_para_bisect, nota_buscar)
    
    if posicion < len(notas_para_bisect) and notas_para_bisect[posicion] == nota_buscar:
        resultado = f"✅ La nota {nota_buscar} se encuentra en la posición {posicion}"
        encontrada = True
    else:
        resultado = f"❌ La nota {nota_buscar} NO está en la lista"
        if posicion < len(notas_para_bisect):
            resultado += f" (se insertaría en posición {posicion})"
        encontrada = False
    
    print(resultado)
    resultados_busqueda.append((nota_buscar, encontrada, posicion))

# Visualizar las búsquedas
plt.figure(figsize=(12, 8))

# Crear gráfico de la lista con búsquedas resaltadas
bars = plt.bar(range(len(notas_para_bisect)), notas_para_bisect, color='lightblue')

# Resaltar las notas encontradas
for nota_buscar, encontrada, posicion in resultados_busqueda:
    if encontrada and posicion < len(notas_para_bisect):
        bars[posicion].set_color('lightgreen')

plt.title('Lista de Calificaciones con Búsquedas Resaltadas')
plt.xlabel('Posición')
plt.ylabel('Calificación')
plt.ylim(0, max(notas_para_bisect) + 2)

# Añadir valores en las barras
for idx, val in enumerate(notas_para_bisect):
    plt.text(idx, val + 0.1, str(val), ha='center', va='bottom')

# Añadir leyenda
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='lightblue', label='Calificaciones normales'),
                  Patch(facecolor='lightgreen', label='Calificaciones encontradas')]
plt.legend(handles=legend_elements)

plt.tight_layout()
plt.show()

# ============================================================================
# PASO 6: ANÁLISIS COMPARATIVO Y CONCLUSIONES
# ============================================================================

print("\n" + "=" * 60)
print("📊 ANÁLISIS COMPARATIVO DE MÉTODOS DE ORDENAMIENTO")
print("=" * 60)

# Crear un resumen comparativo
comparacion_data = {
    'Método': ['Bubble Sort', 'sorted() [Timsort]'],
    'Complejidad': ['O(n²)', 'O(n log n)'],
    'Comparaciones': [comp_bubble, f'~{len(notas_originales) * np.log2(len(notas_originales)):.0f}'],
    'Intercambios': [inter_bubble, f'~{len(notas_originales):.0f}'],
    'Visualización': ['Muy detallada', 'Proceso simulado'],
    'Eficiencia': ['Baja', 'Alta']
}

print("\n📈 TABLA COMPARATIVA:")
print("-" * 80)
for key in comparacion_data:
    print(f"{key:15} | {comparacion_data[key][0]:15} | {comparacion_data[key][1]:15}")
print("-" * 80)

# Crear visualización comparativa final
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

# Comparación de tiempos teóricos
n_values = [5, 10, 15, 20, 25, 30]
bubble_times = [n**2 for n in n_values]
sorted_times = [n * np.log2(n) for n in n_values]

ax1.plot(n_values, bubble_times, 'ro-', label='Bubble Sort O(n²)', linewidth=2)
ax1.plot(n_values, sorted_times, 'bo-', label='sorted() O(n log n)', linewidth=2)
ax1.set_xlabel('Número de elementos (n)')
ax1.set_ylabel('Operaciones teóricas')
ax1.set_title('Comparación de Complejidad Algorítmica')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Estadísticas de nuestro ejemplo
metodos = ['Bubble Sort', 'sorted()']
operaciones = [comp_bubble, pasos_sorted]

bars = ax2.bar(metodos, operaciones, color=['lightcoral', 'lightgreen'])
ax2.set_title('Operaciones Realizadas en Nuestro Ejemplo')
ax2.set_ylabel('Número de Operaciones')

for bar, val in zip(bars, operaciones):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             str(val), ha='center', va='bottom')

# Comparación visual de listas
x_pos = np.arange(len(notas_originales))
width = 0.25

ax3.bar(x_pos - width, notas_originales, width, label='Original', alpha=0.7)
ax3.bar(x_pos, notas_bubble_sort, width, label='Bubble Sort', alpha=0.7)
ax3.bar(x_pos + width, notas_sorted, width, label='sorted()', alpha=0.7)
ax3.set_title('Comparación de Resultados')
ax3.set_xlabel('Posición')
ax3.set_ylabel('Calificación')
ax3.legend()

# Uso de bisect
caracteristicas = ['Inserción\nOrdenada', 'Búsqueda\nEficiente', 'Mantiene\nOrden']
valores = [1, 1, 1]  # Todas las características son beneficiosas

bars = ax4.bar(caracteristicas, valores, color=['gold', 'skyblue', 'lightgreen'])
ax4.set_title('Ventajas de usar bisect')
ax4.set_ylabel('Beneficio')
ax4.set_ylim(0, 1.2)

for bar in bars:
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, 
             '✓', ha='center', va='bottom', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()

# ============================================================================
# REFLEXIÓN FINAL Y CONCLUSIONES
# ============================================================================

print("\n" + "=" * 60)
print("=" * 60)

reflexion = """
📝 ANÁLISIS DE LA EXPERIENCIA PRÁCTICA:

🔍 EFICIENCIA ALGORÍTMICA:
• Bubble Sort (O(n²)): Realizó {comp_bubble} comparaciones e {inter_bubble} intercambios.
  - Ventaja: Muy visual y fácil de entender el proceso paso a paso.
  - Desventaja: Extremadamente ineficiente para listas grandes.
  - Uso recomendado: Solo para fines educativos o listas muy pequeñas.

• sorted() con Timsort (O(n log n)): Mucho más eficiente en la práctica.
  - Ventaja: Optimizado para casos reales, maneja datos parcialmente ordenados.
  - Desventaja: Proceso interno menos visible para el aprendizaje.
  - Uso recomendado: Producción y casos reales.

🎯 VISUALIZACIÓN DEL PROCESO:
• La visualización de Bubble Sort fue extremadamente útil para entender:
  - Cómo se comparan elementos adyacentes
  - Por qué los elementos "burbujean" hacia su posición final
  - El costo real de un algoritmo ineficiente

• La simulación de sorted() ayudó a comprender:
  - Cómo se construye progresivamente una lista ordenada
  - La diferencia conceptual entre algoritmos

⚡ GESTIÓN DE LISTAS ORDENADAS CON BISECT:
• bisect.insort(): Mantiene automáticamente el orden al insertar (O(n))
• bisect.bisect_left(): Búsqueda binaria eficiente (O(log n))
• Fundamental para mantener estructuras de datos ordenadas dinámicamente

🏆 CONCLUSIÓN PRÁCTICA:
Para gestión de calificaciones en un sistema real:
1. Usar sorted() para ordenamiento inicial
2. Usar bisect para inserciones y búsquedas posteriores
3. Reservar visualizaciones como Bubble Sort solo para enseñanza

La combinación de eficiencia algorítmica y visualización educativa
proporciona tanto comprensión conceptual como aplicabilidad práctica.
""".format(comp_bubble=comp_bubble, inter_bubble=inter_bubble)

print(reflexion)

print("\n" + "=" * 60)
print("✅ TALLER COMPLETADO EXITOSAMENTE")
print("=" * 60)
print(f"📊 Datos finales procesados:")
print(f"   • Notas originales: {len(notas_originales)} elementos")
print(f"   • Lista final con nueva nota: {len(notas_para_bisect)} elementos")
print(f"   • Promedio final: {sum(notas_para_bisect)/len(notas_para_bisect):.2f}")
print(f"   • Rango: {min(notas_para_bisect)} - {max(notas_para_bisect)}")
