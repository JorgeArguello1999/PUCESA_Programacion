def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

nombres = ["Ana", "Luis", "Pedro", "Lucía", "María"]
buscar = input("Ingrese el nombre a buscar: ")

pos = busqueda_lineal(nombres, buscar)
if pos != -1:
    print(f"'{buscar}' se encontró en la posición {pos}.")
else:
    print(f"'{buscar}' no se encuentra en la lista.")