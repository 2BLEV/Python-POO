from abc import ABC, abstractmethod

# Clase abstracta Empleado
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

# Clase concreta para empleados a tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

# Clase concreta para empleados por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, horas_trabajadas, tarifa_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

# Uso de las clases
empleado_tiempo_completo = EmpleadoTiempoCompleto(3000)
print(f"Salario del empleado a tiempo completo: {empleado_tiempo_completo.calcular_salario()}")

empleado_por_horas = EmpleadoPorHoras(120, 15)
print(f"Salario del empleado por horas: {empleado_por_horas.calcular_salario()}")
