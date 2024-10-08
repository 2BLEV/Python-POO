class Animal:
    # Método constructor 
    def __init__(self, especie, edad, color, tamaño, habitat):
        # Defino los atributos de instancia 
        self.especie = especie
        self.edad = edad
        self.color = color
        self.tamaño = tamaño
        self.habitat = habitat
        
    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Animal ")
        print("especie: " + self.especie)
        print("edad: " + self.edad)
        print("color: " + self.color)
        print("Cámara: " + self.tamaño)
        print("Batería: " + self.habitat)
        print("-----------------------------------")
    
    #metodo para enceder Animal
    def encender(self):
        self.energia = int(input("Digite la hora en tiempo militar : "))
        if self.energia > 22:
            print("El Animal "+self.especie+"esta dormido")
    
            print("----------------------------------------------")
        else:
            print("El Animal "+self.especie+" esta despierto")
             
# Creamos los objetos a partir de la clase Animal      
animal1 = Animal("Perro", "5", "Marrón", "Mediano", "Doméstico")
animal2 = Animal("Gato", "3", "Negro", "Pequeño", "Doméstico") 
animal3 = Animal("Elefante", "10", "Gris", "Grande", "Sabana") 

# Mostrar los detalles de cada objeto
animal1.mostrar_detalles()
animal1.encender()
animal2.mostrar_detalles()
animal3.mostrar_detalles()