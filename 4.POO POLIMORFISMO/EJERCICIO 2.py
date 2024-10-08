''' Ejercicio 2: Clases de  Vehículos con Polimorfismo
Crea tres clases: Carro, Moto y Bicicleta, cada una con un método descripcion() que describa el marca de vehículo '''

# Clase Padre Vehiculo
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def descripcion(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases hijas")

# Clase Carro que hereda de Vehiculo
class Carro(Vehiculo):
    def __init__(self, marca, modelo, placa):
        super().__init__(marca)  # Llama al constructor de la clase padre
        self.modelo = modelo
        self.placa = placa

    def descripcion(self):
        print("Soy un carro")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")

# Clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca)  # Llama al constructor de la clase padre
        self.modelo = modelo
        self.cilindrada = cilindrada

    def descripcion(self):
        print("Soy una moto")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cilindrada: {self.cilindrada} cc")

# Clase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, tipo):
        super().__init__(marca)  # Llama al constructor de la clase padre
        self.tipo = tipo

    def descripcion(self):
        print("Soy una bicicleta")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo} (montaña, carretera, etc.)")

# Función que muestra la descripción de cualquier tipo de vehículo
def mostrar_descripcion(vehiculo):
    vehiculo.descripcion()

# Instancias de cada clase
objeto_carro = Carro("Toyota", "Corolla", "ABC123")
objeto_moto = Moto("Honda", "CBR600RR", 600)
objeto_bicicleta = Bicicleta("Trek", "Montaña")

# Llamado al método descripcion() para cada objeto
mostrar_descripcion(objeto_carro)
mostrar_descripcion(objeto_moto)
mostrar_descripcion(objeto_bicicleta)
