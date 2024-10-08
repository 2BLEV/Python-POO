class Empleado:
    def __init__(self, nombre, edad, puesto, salario, antiguedad):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        self.salario = salario
        self.antiguedad = antiguedad

     # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del emplado ")
        print("Nombre: " + self.nombre)
        print("edad: " + self.edad)
        print("puesto: " + self.puesto)
        print("salario: " + self.salario)
        print("antiguedad: " + self.antiguedad)
        print("-----------------------------------")
        
# Creación de objetos
empleado1 = Empleado("Juan", "30", "Desarrollador", "3000", "3")
empleado2 = Empleado("Ana", "25", "Diseñadora", "2800", "2")
empleado3 = Empleado("Luis", "40", "Gerente", "5000", "10")

# Ejemplo de uso
empleado1.mostrar_detalles()
empleado2.mostrar_detalles()
empleado3.mostrar_detalles()

