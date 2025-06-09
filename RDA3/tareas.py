from stack import Pila

# Crear una pila con elementos iniciales
pila_original = Pila([1, 2, 3, 4, 5])

# Crear una copia de la pila original
pila_copia = Pila(pila_original.copiar())

# Mostrar la pila original y su copia
print("Operaciones con pilas:")
print(f"Pila original: {pila_original}")
print(f"Copia de la pila: {pila_copia}")
print()

# Is Empty
print("IS EMPTY:")
print(f"¿Está vacía la pila original? {pila_original.is_empty()}")
print(f"¿Está vacía la pila copia? {pila_copia.is_empty()}")
print()

# POP
print("POP:")
print(f"Elemento removido de la pila copia: {pila_copia.pop()}")
print()

# PEEK
print("PEEK:")
print(f"Elemento en el tope de la pila copia (peek): {pila_copia.peek()}")
print()

# PUSH
print("PUSH:")
print(f"Agregando 6 a la pila copia: {pila_copia.push(6)}")
print()

# Iterar sobre la pila copia
print("ITERANDO:")
print("Iterando sobre la pila copia:")
for elemento in pila_copia:
    print(f"  {elemento}")
print()

    
# Original vs Copia
print("COMPARANDO PILAS:")
print(f"Pila original: {pila_original}")
print(f"Pila copia después de operaciones: {pila_copia}")
print()
