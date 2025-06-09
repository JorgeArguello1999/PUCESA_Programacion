class Pila:

    def __init__(self, elementos_iniciales=None):
        """
        Inicializa una nueva pila.
        
        Args:
            elementos_iniciales (iterable, opcional): Elementos para inicializar la pila.
                                                    Se agregan en el orden dado.
        
        Raises:
            TypeError: Si elementos_iniciales no es iterable.
        """
        self._elementos = []
        
        if elementos_iniciales is not None:
            try:
                for elemento in elementos_iniciales:
                    self._elementos.append(elemento)
            except TypeError:
                raise TypeError("elementos_iniciales debe ser un iterable")
    
    def push(self, elemento):
        """
        Agrega un elemento al tope de la pila.
        
        Args:
            elemento: El elemento a agregar (puede ser de cualquier tipo).
        
        Returns:
            Pila: Referencia a la pila para permitir encadenamiento de métodos.
        """
        self._elementos.append(elemento)
        return self
    
    def pop(self):
        """
        Remueve y retorna el elemento del tope de la pila.
        
        Returns:
            El elemento removido del tope de la pila.
        
        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("No se puede hacer pop() en una pila vacía")
        return self._elementos.pop()
    
    def peek(self):
        """
        Retorna el elemento del tope de la pila sin removerlo.
        
        Returns:
            El elemento en el tope de la pila.
        
        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("No se puede hacer peek() en una pila vacía")
        return self._elementos[-1]
    
    def is_empty(self):
        """
        Verifica si la pila está vacía.
        
        Returns:
            bool: True si la pila está vacía, False en caso contrario.
        """
        return len(self._elementos) == 0
    
    def clear(self):
        """
        Remueve todos los elementos de la pila.
        
        Returns:
            Pila: Referencia a la pila para permitir encadenamiento de métodos.
        """
        self._elementos.clear()
        return self
    
    def search(self, elemento):
        """
        Verifica si un elemento está presente en la pila.
        
        Args:
            elemento: El elemento a buscar.
        
        Returns:
            bool: True si el elemento está en la pila, False en caso contrario.
        """
        return elemento in self._elementos
    
    def copiar(self):
        """
        Retorna una copia de los elementos de la pila como lista.
        El primer elemento de la lista es el fondo de la pila.
        
        Returns:
            list: Lista con una copia de todos los elementos.
        """
        return self._elementos.copy()
    
    def __len__(self):
        """Permite usar len() con la pila."""
        return len(self._elementos)
    
    def __bool__(self):
        """Permite usar la pila en contextos booleanos."""
        return not self.is_empty()
    
    def __str__(self):
        """
        Representación en string de la pila para visualización.
        
        Returns:
            str: Representación visual de la pila.
        """
        if self.is_empty():
            return "Pila(vacía)"
        
        elementos_str = ", ".join(str(elemento) for elemento in reversed(self._elementos))
        return f"Pila(tope -> {elementos_str})"
    
    def __repr__(self):
        """
        Representación técnica de la pila para debugging.
        
        Returns:
            str: Representación técnica de la pila.
        """
        return f"Pila({self._elementos})"
    
    def __eq__(self, otra):
        """
        Compara dos pilas por igualdad.
        
        Args:
            otra: Otra pila para comparar.
        
        Returns:
            bool: True si las pilas son iguales, False en caso contrario.
        """
        if not isinstance(otra, Pila):
            return False
        return self._elementos == otra._elementos
    
    def __iter__(self):
        """
        Permite iterar sobre la pila desde el tope hacia el fondo.
        
        Yields:
            Los elementos de la pila desde el tope hacia el fondo.
        """
        for elemento in reversed(self._elementos):
            yield elemento

