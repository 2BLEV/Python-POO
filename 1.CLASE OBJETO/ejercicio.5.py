class FiguraGeometrica:
    def __init__(self, tipo, color, area, salario, lados):
        self.tipo = tipo
        self.color = color
        self.area = area
        self.salario = salario
        self.lados = lados

# Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información de la figura geometrica ")
        print("tipo: " + self.tipo)
        print("color: " + self.color)
        print("area: " + self.area)
        print("salario: " + self.salario)
        print("lados: " + self.lados)
        print("-----------------------------------")

# Creación de objetos
figura1 = FiguraGeometrica("Cuadrado", "Azul", "25", "20", "4")
figura2 = FiguraGeometrica("Triángulo", "Rojo", "15", "18", "3")
figura3 = FiguraGeometrica("Círculo", "Verde", "78.5", "31.4", "0")

# Ejemplo de uso
figura1.mostrar_detalles()
figura2.mostrar_detalles()
figura3.mostrar_detalles()
