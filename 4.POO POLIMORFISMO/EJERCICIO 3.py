''' Ejercicio 3: Animales con Polimorfismo
Crea tres clases: Perro, Gato, y Pájaro, cada una con un método sonido() que haga el sonido correspondiente '''

# Clase Padre Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases hijas")

# Clase Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llama al constructor de la clase padre
        self.raza = raza

    def sonido(self):
        print(f"El perro {self.nombre}, de raza {self.raza}, hace: ¡Guau!")

# Clase Gato que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)  # Llama al constructor de la clase padre
        self.color = color

    def sonido(self):
        print(f"El gato {self.nombre}, de color {self.color}, hace: ¡Miau!")

# Clase Pájaro que hereda de Animal
class Pajaro(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre)  # Llama al constructor de la clase padre
        self.especie = especie

    def sonido(self):
        print(f"El pájaro {self.nombre}, de especie {self.especie}, hace: ¡Pío!")

# Función que muestra el sonido de cualquier tipo de animal
def hacer_sonido(animal):
    animal.sonido()

# Instancias de cada clase
objeto_perro = Perro("Rex", "Labrador")
objeto_gato = Gato("Mimi", "Blanco")
objeto_pajaro = Pajaro("Tweety", "Canario")

# Llamado al método sonido() para cada objeto
hacer_sonido(objeto_perro)
hacer_sonido(objeto_gato)
hacer_sonido(objeto_pajaro)
