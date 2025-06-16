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
        """Añade un elemento a la cola manteniendo el orden de prioridad"""
        if isinstance(item, Cliente):
            # Insertar en la posición correcta según prioridad
            # Prioridad 1 = más urgente, 4 = menos urgente
            inserted = False
            for i, cliente_actual in enumerate(self.items):
                if item.prioridad < cliente_actual.prioridad:
                    self.items.insert(i, item)
                    inserted = True
                    break
            if not inserted:
                self.items.append(item)
        else:
            # Para elementos que no son clientes, comportamiento normal
            self.items.append(item)

    def dequeue(self):
        """Elimina y retorna el elemento con mayor prioridad (o el primero si no hay prioridades)"""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self):
        """Retorna el próximo elemento a ser atendido sin eliminarlo"""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek from empty queue")

    def size(self):
        return len(self.items)

    def mostrar_por_prioridad(self):
        """Muestra los clientes agrupados por prioridad"""
        if self.is_empty():
            return "No hay clientes en cola"
        
        # Agrupar por prioridad
        prioridades = {}
        for cliente in self.items:
            if isinstance(cliente, Cliente):
                if cliente.prioridad not in prioridades:
                    prioridades[cliente.prioridad] = []
                prioridades[cliente.prioridad].append(cliente.nombre)
        
        resultado = "Clientes por prioridad:\n"
        for prioridad in sorted(prioridades.keys()):
            nivel = {1: "Urgente", 2: "Alta", 3: "Media", 4: "Baja"}.get(prioridad, f"Prioridad {prioridad}")
            resultado += f"  {nivel} ({prioridad}): {', '.join(prioridades[prioridad])}\n"
        
        return resultado.strip()

    # Metodos adicionales
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return f"Cola({self.items})"
    
    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return self.size()