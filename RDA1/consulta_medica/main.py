from funciones import mostrar_pacientes, ver_ficha_paciente, agregar_paciente, agregar_consulta

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


while __name__ == '__main__':
    try:
        opcion = int(input(menu))

    except ValueError:
        print("Error, solo numeros")
        continue

    if opcion == 1:
        print("Mostrar pacientes")
        mostrar_pacientes()

    elif opcion == 2:
        print("Ver ficha de paciente")
        ver_ficha_paciente()

    elif opcion == 3:
        print("Agregar paciente")
        agregar_paciente()

    elif opcion == 4:
        print("Agregar consulta")
        agregar_consulta()

    elif opcion == 5:
        print("Salir")
        break

    else:
        print("Opcion no valida")