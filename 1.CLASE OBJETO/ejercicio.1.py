class Celular:
    # Método constructor 
    def __init__(self, marca, modelo, almacenamiento, camara, bateria):
        # Defino los atributos de instancia 
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.camara = camara
        self.bateria = bateria
        
    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del celular")
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Almacenamiento: " + self.almacenamiento)
        print("Cámara: " + self.camara)
        print("Batería: " + self.bateria)
        print("-----------------------------------")
    
    #metodo para enceder celular
    def encender(self):
        self.energia = int(input("Digite el valor de la carga: "))
        if self.energia > 0:
            print("El celular "+self.modelo+" Se puede encender")
            print(f"||||||||{self.energia} % de carga")
            print("----------------------------------------------")
        else:
            print("El celular "+self.modelo+" no se puede encender")
             
# Creamos los objetos a partir de la clase Celular      
celular1 = Celular("Apple", "iPhone 14", "128 GB", "12 MP", "4000mAh")
celular2 = Celular("Samsung", "Galaxy S22", "256 GB", "10 MP", "4500mAh") 
celular3 = Celular("Xiaomi", "Mi 11", "512 GB", "108 MP", "5000mAh") 

# Mostrar los detalles de cada objeto
celular1.mostrar_detalles()
celular1.encender()
celular2.mostrar_detalles()
celular3.mostrar_detalles()
