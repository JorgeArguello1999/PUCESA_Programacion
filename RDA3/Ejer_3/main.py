from stack import Pila, Cola
from stack import Cliente


menu_tareas = """

Mis tareas:

1.- Ver tareas
2.- Añadir tarea
3.- Eliminar tarea
4.- Volver al menú principal

Tu elección: """

pila_tareas = Pila()

def tareas():
    try:
        input_usuario = int(input(menu_tareas))
        if input_usuario == 1:
            if pila_tareas.is_empty():
                print("No tienes tareas pendientes.")
            else:
                print("Tus tareas pendientes son:")
                for tarea in pila_tareas:
                    print(f"- {tarea}")

        elif input_usuario == 2:
            nueva_tarea = input("Introduce la nueva tarea: ")
            pila_tareas.push(nueva_tarea)
            print(f"Tarea '{nueva_tarea}' añadida.")

        elif input_usuario == 3:
            if pila_tareas.is_empty():
                print("No hay tareas para eliminar.")
            else:
                tarea_eliminada = pila_tareas.pop()
                print(f"Tarea '{tarea_eliminada}' eliminada.")
        elif input_usuario == 4:
            return

    except: 
        print("Entrada no válida. Por favor, ingresa un número.")

menu_clientes = """

Clientes:

1.- Ver clientes (prioritarios)
2.- Añadir cliente
3.- Atender cliente
4.- Mostrar clientes pendientes
5.- Volver al menú principal

Tu elección: """

cola_clientes = Cola()

def clientes():
    while True:
        try:
            input_usuario = int(input(menu_clientes))
            print()  # Separador visual

            if input_usuario == 1:
                if cola_clientes.is_empty():
                    print("No hay clientes en la cola.")
                else:
                    print("Clientes en espera (orden de atención):")
                    for idx, cliente in enumerate(cola_clientes, start=1):
                        print(f"  {idx}. {cliente.nombre} (Prioridad: {cliente.prioridad})")

            elif input_usuario == 2:
                nombre_cliente = input("Introduce el nombre del cliente: ").strip()
                if not nombre_cliente:
                    print("El nombre no puede estar vacío.")
                    continue

                prioridad = input("Introduce la prioridad (1: Urgente - 4: Normal): ").strip()
                if not prioridad.isdigit() or not (1 <= int(prioridad) <= 4):
                    print("Prioridad inválida. Debe ser un número entre 1 y 4.")
                    continue

                nuevo_cliente = Cliente(nombre_cliente, int(prioridad))
                cola_clientes.enqueue(nuevo_cliente)
                print(f"Cliente '{nombre_cliente}' añadido con prioridad {prioridad}.")

            elif input_usuario == 3:
                if cola_clientes.is_empty():
                    print("No hay clientes para atender.")
                else:
                    cliente_atendido = cola_clientes.dequeue()
                    niveles = {1: "Urgente", 2: "Alta", 3: "Media", 4: "Normal"}
                    prioridad_txt = niveles.get(cliente_atendido.prioridad, cliente_atendido.prioridad)
                    print(f"Atendiendo a: {cliente_atendido.nombre} (Prioridad: {prioridad_txt})")

            elif input_usuario == 4:
                print(cola_clientes.mostrar_por_prioridad())

            elif input_usuario == 5:
                print("Volviendo al menú principal...\n")
                break

            else:
                print("Opción fuera de rango. Intenta con un número del 1 al 5.")

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número del 1 al 5.")
        except Exception as e:
            print(f"Error inesperado: {e}")


menu_principal = """

Bienvenidos asociados del AKI 

1.- Mis tareas 
2.- Clientes

3.- Salir o Crtl+C

Tu elección: """

def main():
    while True:
        try:
            input_usuario = int(input(menu_principal))

            if input_usuario == 1: tareas()

            elif input_usuario == 2: clientes()

            elif input_usuario == 3:
                print("Saliendo del programa. ¡Hasta luego!")
                break

        except KeyboardInterrupt:
            print("\nSaliendo del programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()

# ------------------------------------------
# Reflexión: ¿Cuándo usar Pilas y cuándo usar Colas?
#
# Las pilas (LIFO: Last In, First Out) son ideales cuando se necesita deshacer operaciones,
# como en editores de texto, navegación hacia atrás en el historial o evaluación de expresiones.
# El último elemento en entrar es el primero en salir.
#
# En cambio, las colas (FIFO: First In, First Out) son perfectas para gestionar procesos que
# requieren orden de llegada, como atención al cliente, impresión de documentos o ejecución de tareas.
# El primer elemento en entrar es el primero en salir.
#
# Elegir entre una pila o una cola depende del tipo de lógica que se quiere modelar:
# ¿necesito retroceder pasos (pila) o atender en orden justo de llegada (cola)?
# ------------------------------------------
