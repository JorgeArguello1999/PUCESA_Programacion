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
    
    try:
        input_usuario = int(input(menu_clientes))

        if input_usuario == 1:
            if cola_clientes.is_empty():
                print("No hay clientes pendientes.")
            else:
                print("Clientes pendientes:")
                cola_clientes = sorted(cola_clientes.items, key=lambda x: x.prioridad)
                for cliente in cola_clientes:
                    print(f"- {cliente}")
        
        elif input_usuario == 2:
            nombre_cliente = input("Introduce el nombre del cliente: ")
            prioridad = int(input("Introduce la prioridad del cliente (1 Urgente - 4 Menos urgente): "))
            nuevo_cliente = Cliente(nombre_cliente, prioridad)
            cola_clientes.enqueue(nuevo_cliente)
            print(f"Cliente '{nombre_cliente}' añadido con prioridad {prioridad}.")
        
        elif input_usuario == 3:
            if cola_clientes.is_empty():
                print("No hay clientes para atender.")
            else:
                cliente_atendido = cola_clientes.dequeue()
                print(f"Cliente atendido: {cliente_atendido.nombre} con prioridad {cliente_atendido.prioridad}.")

        elif input_usuario == 5:
            return

    except Exception as e:
        print(f"Error: {e}")
        print("Entrada no válida. Por favor, ingresa un número.")
        return
    

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