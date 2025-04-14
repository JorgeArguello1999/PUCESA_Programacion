class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
    
    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupacion: {self.ocupacion}"

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupacion: {self.ocupacion}"
    
menu = """
Gestión de personas
1.- Agregar persona
2.- Mostrar personas

99.- Salir

Tu elección: """

database = []

while True:

    eleccion = int(input(menu))
    print()

    if eleccion == 1:
        try:
            database.append(
                Persona(
                    input("Nombre: "),
                    int(input("Edad: ")),
                    input("Ocupación: ")
                )
            )
        except ValueError:
            print("Error: La edad debe ser un número entero.")
            continue
    
    elif eleccion == 2:
        print("Lista de personas:")
        for i in database:
            print(i)
    
    elif eleccion == 99:
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida")