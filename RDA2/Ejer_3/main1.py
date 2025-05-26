from random import randint

# Productos 
def generar_lista_productos(tipo_lista: str, tamaño: int) -> list[int]:
    """
    Genera una lista de productos según el tipo especificado (aleatoria, ascendente, descendente)
    y el tamaño dado.
    :param tipo_lista: Cadena que indica el tipo de lista a generar ('aleatoria', 'ascendente', 'descendente', 'usuario').
    :param tamaño: Entero que indica la cantidad de elementos en la lista.
    :return: Lista de enteros representando los productos.
    :rtype: list[int]
    """
    if tipo_lista == 'aleatoria':
        return [randint(1, 100) for _ in range(tamaño)]

    elif tipo_lista == 'ascendente':
        return list(range(1, tamaño + 1))

    elif tipo_lista == 'descendente':
        return list(range(tamaño, 0, -1))

    elif tipo_lista == 'usuario':
        while True:
            try:
                entrada = input(f'Introduce {tamaño} precios (enteros) separados por comas: ')
                precios = [int(x.strip()) for x in entrada.split(',') if x.strip().isdigit()]

                if len(precios) == tamaño:

                    return precios
                else:
                    print(f"Por favor, introduce exactamente {tamaño} precios.")

            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar números enteros separados por comas.")

    return []

def bubble_sort(arr: list[int]) -> tuple[list[int], int, int]:
    """
    Ordena una lista usando el algoritmo Bubble Sort.
    Este algoritmo recorre repetidamente la lista, compara elementos adyacentes
    y los intercambia si están en el orden incorrecto. Las pasadas se repiten
    hasta que no se necesitan más intercambios, lo que indica que la lista está ordenada.
    Devuelve la lista ordenada, el número de comparaciones y el número de intercambios realizados.
    :param arr: Lista de enteros a ordenar.
    :return: Tupla con la lista ordenada, número de comparaciones e intercambios.
    :rtype: tuple[list[int], int, int]
    """
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparaciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1

    return arr, comparaciones, intercambios

def insertion_sort(arr: list[int]) -> tuple[list[int], int, int]:
    """
    Ordena una lista usando el algoritmo Insertion Sort.
    Este algoritmo construye la lista final ordenada un elemento a la vez.
    Recorre la lista, tomando cada elemento y "insertándolo" en su posición
    correcta dentro de la porción ya ordenada de la lista.
    Devuelve la lista ordenada, el número de comparaciones y el número de intercambios realizados.
    :param arr: Lista de enteros a ordenar.
    :return: Tupla con la lista ordenada, número de comparaciones e intercambios.
    :rtype: tuple[list[int], int, int]
    """
    comparaciones = 0
    intercambios = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            comparaciones += 1 
            arr[j + 1] = arr[j]
            j -= 1
            intercambios += 1 
        arr[j + 1] = key 

        if j >= 0: 
            pass 

    return arr, comparaciones, intercambios

def selection_sort(arr: list[int]) -> tuple[list[int], int, int]:
    """
    Ordena una lista usando el algoritmo Selection Sort.
    Este algoritmo divide la lista en dos partes: una sublista ordenada
    y una sublista no ordenada. Repetidamente encuentra el elemento mínimo
    (o máximo) de la sublista no ordenada y lo mueve al final de la sublista ordenada.
    Devuelve la lista ordenada, el número de comparaciones y el número de intercambios realizados.
    :param arr: Lista de enteros a ordenar.
    :return: Tupla con la lista ordenada, número de comparaciones e intercambios.
    :rtype: tuple[list[int], int, int]
    """
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            intercambios += 1
    return arr, comparaciones, intercambios

def imprimir_salida(algoritmo: str, lista_original: list, algoritmo_func) -> None:
    """
    Imprime los resultados de la ejecución de un algoritmo de ordenamiento.
    Incluye la lista ordenada, el número de comparaciones y el número de intercambios.
    :param algoritmo: Nombre del algoritmo de ordenamiento.
    :param lista_original: La lista original (no modificada) que se va a ordenar.
    :param algoritmo_func: La función del algoritmo de ordenamiento a ejecutar.
    """
    lista = lista_original.copy() # Se crea una copia para no modificar la lista original en cada llamada.
    ordenada, comp, interc = algoritmo_func(lista)
    print(f'{algoritmo} Sort: {ordenada}')
    print(f'Comparaciones: {comp}, Intercambios: {interc}')

def ejecutar_y_mostrar_algoritmo(nombre_algoritmo: str, lista_original: list, algoritmo_func, resultados_dict: dict) -> None:
    """
    Ejecuta un algoritmo de ordenamiento, imprime sus resultados y los almacena en un diccionario.
    :param nombre_algoritmo: Nombre del algoritmo de ordenamiento (ej. "Bubble").
    :param lista_original: La lista original que se va a ordenar.
    :param algoritmo_func: La función del algoritmo de ordenamiento a ejecutar.
    :param resultados_dict: El diccionario donde se almacenarán los resultados.
    """
    lista_copia = lista_original.copy() # Se crea una copia para cada algoritmo
    ordenada, comp, interc = algoritmo_func(lista_copia)
    print(f'{nombre_algoritmo} Sort: {ordenada}')
    print(f'Comparaciones: {comp}, Intercambios: {interc}')
    resultados_dict[nombre_algoritmo] = (ordenada, comp, interc)
    print("--------------------------")

if __name__ == '__main__':
    # Parte 1: Implementación y ejecución con diferentes tipos de listas

    while True:
        try:
            opcion_usuario = input("¿Desea ingresar sus propios precios? (s/n): ").lower()
            if opcion_usuario == 's':
                tipo_lista = 'usuario'
                tamaño_lista = 10 
                productos = generar_lista_productos(tipo_lista, tamaño_lista)
                if not productos: 
                    continue

            elif opcion_usuario == 'n':
                tipo_lista_predefinida = input("Elija el tipo de lista predefinida (aleatoria, ascendente, descendente): ").lower()

                if tipo_lista_predefinida not in ['aleatoria', 'ascendente', 'descendente']:
                    print("Tipo de lista inválido. Por favor, elija entre 'aleatoria', 'ascendente' o 'descendente'.")
                    continue

                tipo_lista = tipo_lista_predefinida
                tamaño_lista = 10
                productos = generar_lista_productos(tipo_lista, tamaño_lista)

            else:
                print("Opción inválida. Por favor, ingrese 's' o 'n'.")
                continue
            break 

        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, inténtelo de nuevo.")

    print(f'\n--- Resultados para lista {tipo_lista} ---')
    print('Lista original:', productos)
    print('--------------------------')

    # Almacenar los resultados para la tabla resumen
    resultados_por_algoritmo = {}

    print("\nResultados detallados por algoritmo:")
    print("-----------------------------------")

    # Ejecutar y mostrar resultados para cada algoritmo usando la nueva función
    ejecutar_y_mostrar_algoritmo("Bubble", productos, bubble_sort, resultados_por_algoritmo)
    ejecutar_y_mostrar_algoritmo("Insertion", productos, insertion_sort, resultados_por_algoritmo)
    ejecutar_y_mostrar_algoritmo("Selection", productos, selection_sort, resultados_por_algoritmo)

    print("\n--- Resumen de rendimientos ---")
    print(f"{'Algoritmo':<10} {'Comparaciones':<15} {'Intercambios'}")
    for nombre, (lista_ord, comp, interc) in resultados_por_algoritmo.items():
        print(f"{nombre:<10} {comp:<15} {interc}")


    # Parte 2: Explicación y análisis (en una celda Markdown, aquí como comentario extenso)

"""
# ¿Cómo funciona cada algoritmo?
- Bubble Sort: Compara y "burbujea" los elementos grandes al final, intercambiando pares adyacentes repetidamente hasta que la lista está ordenada. Es simple pero ineficiente.

- Insertion Sort: Construye la lista ordenada un elemento a la vez, insertando cada nuevo elemento en su posición correcta dentro de la parte ya ordenada. Eficiente para listas pequeñas o casi ordenadas.

- Selection Sort: Encuentra el elemento más pequeño en la parte no ordenada de la lista y lo intercambia con el primer elemento de esa parte, repitiendo hasta que toda la lista está ordenada. Minimiza el número de intercambios.

# Comparación de Rendimientos y ¿Cuál fue más eficiente?
Para listas pequeñas (10 elementos), la eficiencia puede variar:

- Comparaciones: Bubble Sort y Selection Sort tienden a realizar más comparaciones. Insertion Sort puede ser más eficiente si la lista está parcialmente ordenada.

- Intercambios: Bubble Sort realiza muchos intercambios. Insertion Sort realiza "desplazamientos". Selection Sort realiza el menor número de intercambios (N-1).

- En general, Insertion Sort suele ser más eficiente para listas pequeñas y aleatorias. Selection Sort destaca por su bajo número de intercambios, y Bubble Sort es el menos eficiente en la mayoría de los casos.

# ¿En qué situaciones usarías cada uno?
- Bubble Sort: Principalmente para fines educativos debido a su simplicidad; rara vez en aplicaciones prácticas por su ineficiencia.

- Insertion Sort: Ideal para listas pequeñas, listas que ya están casi ordenadas, o como parte de algoritmos de ordenamiento más complejos (híbridos). Ejemplo: ordenar una mano de cartas.

- Selection Sort: Útil cuando el costo de un intercambio de datos es muy alto (minimizando las escrituras) o cuando se necesita garantizar el número mínimo de movimientos de elementos.
"""