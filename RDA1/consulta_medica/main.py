separador = "-"*33

menu = f"""
{separador}

<< MedTec >>

{separador}

    1. Mostrar pacientes
    2. Ver ficha de paciente
    3. Agregar paciente
    4. Agregar consulta

    5. Salir

{separador}
Tu eleccion: """


while True:
    try:
        opcion = int(input(menu))

    except ValueError:
        print("Error, solo numeros")
        continue

    if opcion == 1:
        print("Mostrar pacientes")

    elif opcion == 2:
        print("Ver ficha de paciente")

    elif opcion == 3:
        print("Agregar paciente")

    elif opcion == 4:
        print("Agregar consulta")

    elif opcion == 5:
        print("Salir")
        break

    else:
        print("Opcion no valida")