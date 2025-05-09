"""
Ejercicio 1: Búsqueda lineal
"""

def busqueda_lineal(lista: list, objetivo: str, contador: int = 0) -> list:
    """
    Realiza una búsqueda lineal en una lista.\n
    param lista: Lista de elementos (frutas).\n
    param objetivo: Elemento a buscar en la lista.\n
    param contador: Contador de comparaciones (opcional por defecto 0).\n
    return: Lista con el resultado de la búsqueda [True/False, posición, comparaciones]\n
    """
    for i in range(len(lista)):
        contador += 1
        if lista[i].lower() == objetivo.lower():
            return [True, i, contador]
    return [False, -1, contador]


frutas = ["Manzana", "Banana", "Naranja", "Sandia", "Melon", "Uva", "Melocoton", "Mango", "Papaya", "Fresa"]

while True:
    print('\n' * 8)
    print("Bienvenido a la búsqueda lineal de frutas.")
    try:
        print("Lista de frutas:", frutas)
        print("Para salir del programa, presione Ctrl+C.")
        buscar = input("Ingrese el nombre de la fruta a buscar: ").strip().title()

        resultado = busqueda_lineal(frutas, buscar)
        if resultado[0]:
            print(f"'{buscar}' se encontró en la posición {resultado[1]}, con {resultado[2]} comparaciones.")
        else:
            print(f"'{buscar}' no se encuentra en la lista. Comparaciones realizadas: {resultado[2]}")

    except KeyboardInterrupt:
        print("\nSaliendo del programa.")
        break
