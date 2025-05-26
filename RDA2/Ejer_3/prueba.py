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

    # Bubble Sort
    lista_bubble = productos.copy()
    ordenada_bubble, comp_bubble, interc_bubble = bubble_sort(lista_bubble)
    print(f'Bubble Sort: {ordenada_bubble}')
    print(f'Comparaciones: {comp_bubble}, Intercambios: {interc_bubble}')
    resultados_por_algoritmo["Bubble"] = (ordenada_bubble, comp_bubble, interc_bubble)
    print("--------------------------")

    # Insertion Sort
    lista_insertion = productos.copy()
    ordenada_insertion, comp_insertion, interc_insertion = insertion_sort(lista_insertion)
    print(f'Insertion Sort: {ordenada_insertion}')
    print(f'Comparaciones: {comp_insertion}, Intercambios: {interc_insertion}')
    resultados_por_algoritmo["Insertion"] = (ordenada_insertion, comp_insertion, interc_insertion)
    print("--------------------------")

    # Selection Sort
    lista_selection = productos.copy()
    ordenada_selection, comp_selection, interc_selection = selection_sort(lista_selection)
    print(f'Selection Sort: {ordenada_selection}')
    print(f'Comparaciones: {comp_selection}, Intercambios: {interc_selection}')
    resultados_por_algoritmo["Selection"] = (ordenada_selection, comp_selection, interc_selection)
    print("--------------------------")

    print("\n--- Resumen de rendimientos ---")
    print(f"{'Algoritmo':<10} {'Comparaciones':<15} {'Intercambios'}")
    for nombre, (lista_ord, comp, interc) in resultados_por_algoritmo.items():
        print(f"{nombre:<10} {comp:<15} {interc}")


    # Parte 2: Explicación y análisis (en una celda Markdown, aquí como comentario extenso)

    """
    ## Explicación y análisis de los Métodos de Ordenamiento

    ### ¿Cómo funciona cada algoritmo?

    * Bubble Sort (Ordenamiento de Burbuja):
        Este algoritmo funciona "burbujeando" los elementos más grandes a su posición correcta al final de la lista en cada pasada. Recorre la lista repetidamente, comparando cada par de elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que ya no se realizan intercambios en una pasada completa, lo que significa que la lista está ordenada. Es intuitivo pero generalmente ineficiente para listas grandes.

    * Insertion Sort (Ordenamiento por Inserción):
        Insertion Sort construye la lista ordenada un elemento a la vez. Comienza asumiendo que el primer elemento ya está ordenado. Luego, toma cada elemento restante de la lista y lo "inserta" en su posición correcta dentro de la porción ya ordenada de la lista. Esto se hace desplazando los elementos mayores que el elemento a insertar una posición a la derecha. Es eficiente para listas pequeñas o listas que ya están casi ordenadas.

    * Selection Sort (Ordenamiento por Selección):
        Selection Sort funciona dividiendo la lista en dos partes: una sublista de elementos ordenados y una sublista de elementos sin ordenar. En cada iteración, el algoritmo encuentra el elemento más pequeño (o más grande, dependiendo del orden) en la sublista no ordenada y lo intercambia con el primer elemento de la sublista no ordenada. De esta manera, el elemento mínimo se "selecciona" y se coloca en su posición final. Este proceso se repite hasta que toda la lista está ordenada.

    ### Comparación de Rendimientos: ¿Cuál fue más eficiente y por qué?

    En mi caso, para una lista pequeña (10 elementos), la eficiencia puede variar ligeramente dependiendo de la disposición inicial de los números. Sin embargo, en general, observaremos patrones consistentes:

    * Comparaciones:
        * Bubble Sort y Selection Sort tienden a realizar un número de comparaciones similar y a menudo más alto, especialmente para listas aleatorias o inversamente ordenadas. Esto se debe a sus bucles anidados que recorren una gran parte de la lista en cada iteración.
        * Insertion Sort puede ser más eficiente en términos de comparaciones si la lista está parcialmente ordenada o es pequeña, ya que su bucle interno se detiene tan pronto como encuentra la posición correcta para el elemento.

    * Intercambios:
        * Bubble Sort suele realizar muchos intercambios, ya que mueve los elementos paso a paso a través de la lista. Esto lo hace menos eficiente en situaciones donde los elementos están muy desordenados.
        * Insertion Sort realiza un número de "desplazamientos" que son equivalentes a intercambios, pero a menudo son menos costosos que los intercambios directos de Bubble Sort, especialmente cuando los elementos ya están cerca de su posición final.
        * Selection Sort realiza el menor número de intercambios, ya que solo realiza un intercambio por cada pasada del bucle exterior (es decir, N-1 intercambios en total para una lista de N elementos). Esto lo hace ventajoso en situaciones donde el costo de un intercambio es muy alto.

    Conclusión de Eficiencia:
    Para listas pequeñas y aleatorias, Insertion Sort a menudo muestra un buen rendimiento en términos de comparaciones y un número razonable de intercambios. Selection Sort es notable por su bajo número de intercambios, lo cual puede ser crucial en ciertas aplicaciones. Bubble Sort es casi siempre el menos eficiente de los tres para cualquier tipo de lista (excepto una lista ya ordenada, donde Insertion Sort también brilla).

    ### ¿En qué situaciones usarías cada uno en la vida real o en software?

    * Bubble Sort:
        * Vida Real: Raramente se usa en la práctica debido a su ineficiencia. Podría ser útil para enseñar conceptos básicos de ordenamiento debido a su simplicidad y fácil visualización.
        * Software: Muy limitado. Quizás en situaciones donde la simplicidad del código es la máxima prioridad y el tamaño de la lista es extremadamente pequeño (menos de 10 elementos) y el rendimiento no es crítico.

    * Insertion Sort:
        * Vida Real:
            * Ordenando una mano de cartas: cuando recibes una nueva carta, la insertas en la posición correcta en tu mano ya ordenada.
            * Organizar libros en un estante donde ya tienes algunos libros ordenados y añades nuevos.
        * Software:
            * Listas pequeñas: Es muy eficiente para listas con un número reducido de elementos.
            * Listas casi ordenadas: Si se sabe que la lista de entrada está casi ordenada, Insertion Sort es extremadamente rápido porque realiza muy pocos desplazamientos.
            * Como parte de algoritmos híbridos: Muchos algoritmos de ordenamiento más avanzados (como Timsort o Introsort) usan Insertion Sort para ordenar pequeñas sublistas o para la fase final del ordenamiento.

    * Selection Sort:
        * Vida Real:
            * Encontrar el artículo más barato de un catálogo y colocarlo al principio, luego el segundo más barato, etc.
            * Podría usarse en una competencia donde se selecciona al ganador y se le da el primer premio, luego al siguiente y así sucesivamente.
        * Software:
            * Cuando el costo de intercambio es muy alto: Si la escritura de datos a memoria es significativamente más costosa que la lectura (por ejemplo, en memoria flash o discos duros), Selection Sort es una buena opción porque minimiza el número de escrituras.
            * Garantizar un número mínimo de intercambios: Si se necesita asegurar que el número de movimientos de elementos sea el menor posible, Selection Sort es el candidato.
    """