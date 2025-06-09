from stack import Pila

historial = Pila()
menu = f"""
{"-"*33}
\tHistorial de Navegación
1. Visitar nueva página
2. Ir atrás
3. Ver página actual
4. Ver historial
5. Salir
{"-"*33}

Seleccione una opción (1-5): """

def visitar_pagina(pagina):
    """Agrega una nueva página al historial."""
    historial.push(pagina)
    print(f"Página '{pagina}' visitada y agregada al historial.")
    return True

def ir_atras():
    """Elimina la última página visitada del historial."""
    if not historial.is_empty():
        pagina = historial.pop()
        print(f"Regresaste a la página '{pagina}'.")
    else:
        print("No hay páginas en el historial para regresar.")

def ver_pagina_actual():
    """Muestra la página actual (última visitada)."""
    if not historial.is_empty():
        pagina_actual = historial.peek()
        print(f"Página actual: '{pagina_actual}'")

    else:
        print("No hay páginas en el historial.")
    
def ver_historial():
    """Muestra todo el historial de navegación."""
    if not historial.is_empty():
        print("Historial de navegación:")
        for pagina in historial:
            print(f"- {pagina}")
    else:
        print("El historial está vacío.")

def main():
    while True:
        print(f"Tu historial de navegación es: {historial}")

        try:
            opcion = int(input(menu))

            if opcion == 1:
                pagina = input("Ingresa la URL de la nueva página: ")
                visitar_pagina(pagina)

            elif opcion == 5:
                print("Saliendo del programa...")
                break

            elif opcion == 2: ir_atras()

            elif opcion == 3: ver_pagina_actual()

            elif opcion == 4: ver_historial()
            
            else: raise ValueError("Opción no válida. Por favor, elige un número entre 1 y 5.")

        except KeyboardInterrupt:
            print("\nSaliendo del programa...")
            break

        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

    return 0

if __name__ == "__main__": 
    main()