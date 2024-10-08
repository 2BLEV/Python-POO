class Moto:
    def __init__(self, marca, modelo, cilindrada, color, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.color = color
        self.velocidad_maxima = velocidad_maxima

   # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del moto")
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Cilindriaca: " + self.cilindrada)
        print("Color: " + self.color)
        print("Velocidad maxima: " + self.velocidad_maxima)
        print("-----------------------------------")

# Creación de objetos
moto1 = Moto("Yamaha", "R6", "600cc", "Negra", "250")
moto2 = Moto("Ducati", "Panigale", "1100cc", "Roja", "299")
moto3 = Moto("Kawasaki", "Ninja", "1000cc", "Verde", "290")

# Ejemplo de uso
moto1.mostrar_detalles()
moto2.mostrar_detalles()
moto2.mostrar_detalles()
