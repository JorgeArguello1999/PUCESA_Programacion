class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion 
    
    def descripcion(self):
        return f"{self.nombre} tiene {self.edad} años y trabaja como {self.ocupacion}"
    
    def mayor_edad(self):
        return self.edad >= 18
    
def mostrar_menu():
    return int(input(f"""
Gestión de personas
1.- Agregar persona
2.- Mostrar personas
3.- Buscar persona
4.- Salir

Tu elección: """))
    
personas = []

while True:
    eleccion = mostrar_menu()
    if eleccion < 1 or eleccion > 4:
        print("Opción no válida")
        continue
    
    if eleccion == 1:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        ocupacion = input("Ocupación: ")
        persona = Persona(nombre, edad, ocupacion)
        personas.append(persona)
        print(f"Persona {nombre} agregada")
    
    elif eleccion == 2:
        if not personas:
            print("No hay personas en la lista")
        else:
            print("Lista de personas:")
            for persona in personas:
                print(persona.descripcion())
    
    elif eleccion == 3:
        nombre = input("Nombre de la persona a buscar: ")
        encontrada = False
        
        for persona in personas:
            if persona.nombre.lower() == nombre.lower():
                print(persona.descripcion())
                encontrada = True
                break
        if not encontrada:
            print(f"No se encontró a {nombre} en la lista")

    elif eleccion == 4:
        print("Saliendo del programa...")
        break