class Cliente():
    # Estructura de datos para los clientes
    def __init__(self, nombre:str, prioridad:int=0):
        self.nombre = nombre 
        self.prioridad = prioridad     
    
    def __str__(self):
        return f"Cliente: {self.nombre}, Prioridad: {self.prioridad}"
    
    def __repr__(self):
        return f"Cliente(nombre={self.nombre}, prioridad={self.prioridad})"
    
    def __getitem__(self, key):
        if key == 'nombre':
            return self.nombre
        elif key == 'prioridad':
            return self.prioridad
        else:
            raise KeyError(f"'{key}' no es un atributo válido de Cliente")

class Pila():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    # Metodos adicionales
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return f"Pila({self.items})"
    
    def __iter__(self):
        items = self.items[::-1]
        return iter(items)
    
    def __len__(self):
        return self.size()

class Cola():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek from empty queue")

    def size(self):
        return len(self.items)

    # Metodos adicionales
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return f"Cola({self.items})"
    
    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return self.size()