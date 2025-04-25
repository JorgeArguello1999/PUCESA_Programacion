from paciente import Paciente, Consulta
from datetime import datetime

# Lista global de pacientes
pacientes = []

def mostrar_pacientes() -> None:
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    print("\n--- Lista de pacientes ---")
    for idx, paciente in enumerate(pacientes, start=1):
        status = "Válido" if paciente.check_paciente() else "Inválido"
        print(f"{idx}. Cédula: {paciente.cedula}, Edad: {paciente.edad}, Tipo de sangre: {paciente.tipo_sangre} - {status}")
    print("--------------------------\n")


def ver_ficha_paciente() -> None:
    cedula = input("Ingrese la cédula del paciente: ").strip()
    for paciente in pacientes:
        if paciente.cedula == cedula:
            info = paciente.devolver()
            print(f"\n--- Ficha del paciente {info['cedula']} ---")
            print(f"Edad: {info['edad']}")
            print(f"Tipo de sangre: {info['tipo_sangre']}")
            if not paciente.check_paciente():
                print("! Atención: Algunos datos del perfil no son válidos.")
            if info['citas_medicas']:
                print("Historial de consultas:")
                for c in info['citas_medicas']:
                    fecha = c['fecha'].strftime("%Y-%m-%d %H:%M:%S")
                    print(f"- Fecha: {fecha}, Diagnóstico: {c['diagnostico']}, Tratamiento: {c['tratamiento']}")
            else:
                print("No hay consultas registradas para este paciente.")
            print("------------------------------\n")
            return
    print("Paciente no encontrado.\n")


def agregar_paciente():
    print("\n--- Agregar nuevo paciente ---")
    while True:
        try:
            cedula = input("Cédula (10 dígitos): ").strip()
            edad_input = input("Edad: ").strip()
            edad = int(edad_input)
            tipo_sangre = input("Tipo de sangre (A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip()

            paciente = Paciente(cedula, edad, tipo_sangre)
            if paciente.check_paciente():
                pacientes.append(paciente)
                print("Paciente agregado correctamente.\n")
                return
            
            else:
                raise Exception("Datos inválidos")

        except ValueError:
            print("Error al agregar paciente. Verifique los datos e intente nuevamente.\n")
            continue


def agregar_consulta():
    print("\n--- Agregar consulta a paciente ---")
    cedula = input("Ingrese la cédula del paciente: ").strip()
    for paciente in pacientes:
        if paciente.cedula == cedula:
            diagnostico = input("Diagnóstico: ").strip()
            tratamiento = input("Tratamiento: ").strip()
            fecha_input = input("Fecha (YYYY-MM-DD HH:MM) o dejar vacío para fecha actual: ").strip()
            fecha = None
            if fecha_input:
                try:
                    fecha = datetime.strptime(fecha_input, "%Y-%m-%d %H:%M")
                except ValueError:
                    print("Formato de fecha inválido. Se usará la fecha y hora actual.")
            consulta = Consulta(diagnostico, tratamiento, fecha)
            if paciente.agregar_cita(consulta):
                print("Consulta agregada correctamente.\n")
            else:
                print("Error al agregar consulta.\n")
            return
    print("Paciente no encontrado.\n")