from datetime import datetime

class Consulta:
    def __init__(self, diagnostico: str, tratamiento: str, fecha=None) -> None:
        self.fecha = fecha or datetime.now()
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    def devolver(self) -> dict:
        return {
            "fecha": self.fecha,
            "diagnostico": self.diagnostico,
            "tratamiento": self.tratamiento
        }


class Paciente:
    def __init__(self, cedula: str, edad: int, tipo_sangre: str) -> None:
        self.cedula = self.validar_cedula(cedula)
        self.edad = self.validar_edad(edad)
        self.tipo_sangre = self.validar_sangre(tipo_sangre)
        self.citas_medicas = []

        if self.cedula != "" and self.tipo_sangre != "":
            print("Paciente creado correctamente")

    # Validaciones
    def validar_cedula(self, cedula: str) -> str:
        if len(cedula) == 10:
            try:
                int(cedula)
                return cedula
            except Exception as e:
                print("Error, solo numeros")
                print(str(e))

        print("Error, cedula no cumple 10 caracteres")
        return ""

    def validar_edad(self, edad: int) -> int:
        if edad >= 0 or edad <= 110:
            return edad
        print("Error, edad fuera del limite 0-110")
        return 0

    def validar_sangre(self, tipo_sangre: str) -> str:
        sangre_tipos = ["A+", "A-" "B+", "B-", "AB+", "AB-", "O+", "O-"]

        if tipo_sangre.upper() in sangre_tipos:
            return tipo_sangre.upper()

        print(f"Error, tipo de sangre no valido: {sangre_tipos}")
        return ""

    # Citas medicas
    def agregar_cita(self, consulta: Consulta):
        self.citas_medicas.append(consulta.devolver())

    # Checkear paciente 
    def check_paciente(self) -> bool:
        if self.cedula != "" and self.tipo_sangre != "":
            return True
        return False
    
    # Mostrar 
    def devolver(self) -> dict:
        return {
            "cedula": self.cedula,
            "edad": self.edad,
            "tipo_sangre": self.tipo_sangre,
            "citas_medicas": self.citas_medicas
        }