separador = 22*"-"

menu = f"""

{separador}

1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir

{separador}

5.- Salir
{separador}

Tu elección: """

elecccion = int(input(menu))
if elecccion < 1 or elecccion > 5:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if elecccion == 1:
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")

    elif elecccion == 2: 
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")

    elif elecccion == 3:
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")

    elif elecccion == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("No se puede dividir entre cero")

    elif elecccion == 5 :
        print("Saliendo del programa...")

            
else:
    print("Opción no válida. Por favor, elige una opción del menú.")
