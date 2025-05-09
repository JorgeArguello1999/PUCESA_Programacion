"""
Ejercicio 2: Búsqueda binaria
"""

def busqueda_binaria(lista:list, objetivo:int, contador:int=0) -> list:
    """
    Realiza una búsqueda binaria en una lista ordenada.\n
    param lista: Lista ordenada de elementos.\n
    param objetivo: Elemento a buscar en la lista.\n
    param contador: Contador de iteraciones (opcional por defecto 0).\n
    return: Tupla con el resultado de la búsqueda (True/False), posición del elemento y número de iteraciones.\n
    [True/False, posición, iteraciones]
    """

    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        contador += 1
        medio = (inicio + fin) // 2

        if lista[medio] == objetivo:
            return True, medio, contador

        elif lista[medio] < objetivo:
            inicio = medio + 1

        else:
            fin = medio - 1
    return False, 0, contador

numeros = [ i*10 for i in range(1, 11)]
while True:
    print('\n'*8)
    print("Bienvenido a la búsqueda binaria.")
    try:
        print("Lista de números:", numeros)
        print("Para salir del programa, presione Ctrl+C.")
        buscar = int(input("Ingrese el número a buscar: "))

        pos = busqueda_binaria(numeros, buscar)
        if pos[0]:
            print(f"'{buscar}' se encontró en la posición {pos[2]}, con {pos[1]} iteraciones.")
        else:
            print(f"'{buscar}' no se encuentra en la lista.")

    except ValueError:
        print("Error: Debe ingresar un número entero.")
    
    except KeyboardInterrupt:
        print("\nSaliendo del programa.")
        break