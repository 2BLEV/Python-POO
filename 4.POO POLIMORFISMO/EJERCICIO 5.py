'''Ejercicio 5: Clases de Profesiones con Polimorfismo
Crea tres clases: Médico, Ingeniero, y Docente, cada una con un método trabajar() que describa la información técnica del profesional. '''
# Clase Padre Profesional
class Profesional:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def trabajar(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases hijas")

# Clase Médico que hereda de Profesional
class Medico(Profesional):
    def __init__(self, nombre, especialidad, hospital):
        super().__init__(nombre, especialidad)  # Llama al constructor de la clase padre
        self.hospital = hospital

    def trabajar(self):
        print(f"El médico {self.nombre}, especializado en {self.especialidad}, trabaja en el hospital {self.hospital} atendiendo a los pacientes.")

# Clase Ingeniero que hereda de Profesional
class Ingeniero(Profesional):
    def __init__(self, nombre, especialidad, empresa):
        super().__init__(nombre, especialidad)  # Llama al constructor de la clase padre
        self.empresa = empresa

    def trabajar(self):
        print(f"El ingeniero {self.nombre}, especializado en {self.especialidad}, trabaja en la empresa {self.empresa} diseñando y desarrollando proyectos.")

# Clase Docente que hereda de Profesional
class Docente(Profesional):
    def __init__(self, nombre, especialidad, instituto):
        super().__init__(nombre, especialidad)  # Llama al constructor de la clase padre
        self.instituto = instituto

    def trabajar(self):
        print(f"El docente {self.nombre}, especializado en {self.especialidad}, trabaja en el instituto {self.instituto} enseñando a los estudiantes.")

# Función que muestra la información técnica de cualquier profesional
def trabajar_profesional(profesional):
    profesional.trabajar()

# Instancias de cada clase
objeto_medico = Medico("Dr. Juan Pérez", "Cardiología", "Hospital Central")
objeto_ingeniero = Ingeniero("Ing. María García", "Ingeniería Civil", "Constructora ABC")
objeto_docente = Docente("Prof. Carlos Fernández", "Matemáticas", "Escuela Nacional")

# Llamado al método trabajar() para cada objeto
trabajar_profesional(objeto_medico)
trabajar_profesional(objeto_ingeniero)
trabajar_profesional(objeto_docente)

