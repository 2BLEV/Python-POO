from abc import ABC, abstractmethod

# Clase abstracta TareaEmpleado
class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

# Clase concreta Ingeniero
class Ingeniero(TareaEmpleado):
    def realizar_tarea(self):
        return "El ingeniero está diseñando un puente."

# Clase concreta Doctor
class Doctor(TareaEmpleado):
    def realizar_tarea(self):
        return "El doctor está diagnosticando a un paciente."

# Uso de las clases
ingeniero = Ingeniero()
print(ingeniero.realizar_tarea())

doctor = Doctor()
print(doctor.realizar_tarea())
