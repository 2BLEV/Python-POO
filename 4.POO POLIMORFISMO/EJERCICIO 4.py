''' Ejercicio 4: Instrumentos Musicales con Polimorfismo
Crea clases: Guitarra, Piano, y Trompeta, cada una con un método tocar() que describa la información técnica del instrumento. '''
# Clase Padre Instrumento
class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases hijas")

# Clase Guitarra que hereda de Instrumento
class Guitarra(Instrumento):
    def __init__(self, nombre, cuerdas, tipo):
        super().__init__(nombre)  # Llama al constructor de la clase padre
        self.cuerdas = cuerdas
        self.tipo = tipo

    def tocar(self):
        print(f"La guitarra {self.nombre} tiene {self.cuerdas} cuerdas y es de tipo {self.tipo}. Se toca rasgando o punteando las cuerdas.")

# Clase Piano que hereda de Instrumento
class Piano(Instrumento):
    def __init__(self, nombre, teclas, tipo):
        super().__init__(nombre)  # Llama al constructor de la clase padre
        self.teclas = teclas
        self.tipo = tipo

    def tocar(self):
        print(f"El piano {self.nombre} tiene {self.teclas} teclas y es de tipo {self.tipo}. Se toca presionando las teclas.")

# Clase Trompeta que hereda de Instrumento
class Trompeta(Instrumento):
    def __init__(self, nombre, material):
        super().__init__(nombre)  # Llama al constructor de la clase padre
        self.material = material

    def tocar(self):
        print(f"La trompeta {self.nombre} está hecha de {self.material}. Se toca soplando y utilizando los pistones.")

# Función que muestra la información técnica de cualquier instrumento
def tocar_instrumento(instrumento):
    instrumento.tocar()

# Instancias de cada clase
objeto_guitarra = Guitarra("Fender Stratocaster", 6, "Eléctrica")
objeto_piano = Piano("Yamaha C3", 88, "De cola")
objeto_trompeta = Trompeta("Bach Stradivarius", "Latón")

# Llamado al método tocar() para cada objeto
tocar_instrumento(objeto_guitarra)
tocar_instrumento(objeto_piano)
tocar_instrumento(objeto_trompeta)
