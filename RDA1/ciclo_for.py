# Tabla de multiplicar
for x in range(1, 11):
    for y in range(1, 11):
        print(f"{x} x {y} = {x*y}")
    print("-"*20)

# Operaciones con listas
for i in [1, 2, 3, 4, 5, 6]:
    print(i**2)

# Impar o par
print()
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numeros:
    if i%2 == 0:
        print(f"{i} es par")
    else:   
        print(f"{i} es impar")
    
    
print()
for i in range(2):
    result = "impar"
    if i == 0:
        result = "Par"

    for j in numeros:
        if j%2 == i:
            print(f"{j} es {result}")
        
    
print()
for i in range(0, 6):
    print()
    for j in range(0, 6):
        for k in range(0, 6):
            print(f"{i}*{j}*{k} = {i*j*k}")


print()
for i in [10, 200, 38]:
    for j in [10, 200, 38]:
        print(f"{i}*{j} = {i*j}")

print()
for i in range(2):
    result = "impar"
    if i == 0:
        result = "Par"

    for j in range(0, 11):
        if j%2 == i:
            print(f"{j} es {result}")
        