from random import randint

# Productos 
def generar_lista_productos(default=True) -> list[int]:
    """
    Genera una lista de 10 productos con valores aleatorios entre 1 y 10.
    :return: Lista de enteros representando los productos.
    :rtype: list[int]
    """
    if not default:
        entrada = input('Introduce 10 precios (enteros) separados por comas: ')
        return [int(x.strip()) for x in entrada.split(',') if x.strip().isdigit()]

    return [randint(1, 10) for _ in range(10)]

def bubble_sort(arr:list[int]) -> tuple[list[int], int, int]:
    """
    Ordena una lista usando el algoritmo Bubble Sort.
    Devuelve la lista ordenada, el número de comparaciones y el número de intercambios realizados.
    :param arr: Lista de enteros a ordenar.
    :return: Tupla con la lista ordenada, número de comparaciones e intercambios.
    :rtype: tuple[list[int], int, int]
    """
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambios += 1
    return arr, comparaciones, intercambios

def insertion_sort(arr:list[int]) -> tuple[list[int], int, int]:
    """
    Ordena una lista usando el algoritmo Insertion Sort.
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
            comparaciones += 1
    return arr, comparaciones, intercambios

def selection_sort(arr:list[int]) -> tuple[list[int], int, int]:
    """
    Ordena una lista usando el algoritmo Selection Sort.
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
        for j in range(i+1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            intercambios += 1
    return arr, comparaciones, intercambios

def imprimir_salida(algoritmo:str, lista_original:list, algoritmo_func) -> None:
    lista = lista_original.copy()
    ordenada, comp, interc = algoritmo_func(lista)
    print(f'{algoritmo} Sort:', ordenada)
    print(f'Comparaciones: {comp}, Intercambios: {interc}')


if __name__ == '__main__':
    # Generar lista de productos
    productos = generar_lista_productos()

    print('Lista original:', productos)
    print('--------------------------')
    # Imprimir resultados de cada algoritmo
    imprimir_salida('Bubble', productos, bubble_sort)
    imprimir_salida('Insertion', productos, insertion_sort)
    imprimir_salida('Selection', productos, selection_sort)
    print('--------------------------')
    print('\n'*2)


    resultados = {
        "Bubble": bubble_sort(productos.copy()),
        "Insertion": insertion_sort(productos.copy()),
        "Selection": selection_sort(productos.copy())
    }

    print("\nResumen de rendimientos:")
    print(f"{'Algoritmo':<10} {'Comparaciones':<15} {'Intercambios'}")
    for nombre, (lista, comp, interc) in resultados.items():
        print(f"{nombre:<10} {comp:<15} {interc}")
