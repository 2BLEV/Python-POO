class Carro:
    def __init__(self, marca, modelo, color, motor, capacidad_baul):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.capacidad_baul = capacidad_baul

     # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del carro ")
        print("marca: " + self.marca)
        print("modelo: " + self.modelo)
        print("color: " + self.color)
        print("motor: " + self.motor)
        print("capacidad del baul: " + self.capacidad_baul)
        print("-----------------------------------")

# Creación de objetos
carro1 = Carro("Toyota", "Corolla", "Blanco", "2.0L", "470")
carro2 = Carro("Ford", "Mustang", "Rojo", "5.0L", "380")
carro3 = Carro("Honda", "Civic", "Negro", "1.5L", "420")

# Ejemplo de uso
carro1.mostrar_detalles()
carro2.mostrar_detalles()
carro3.mostrar_detalles()
