class Dispositivo:
    #constructor
    def __init__(self, marca, modelo, año):
      self.marca = marca
      self.modelo = modelo
      self.año = año
      self.capacidad_bateria = int(input("Capacidad de la bateria mAh:"))
    #metodos público
    def registrar(self):
         print ("---- ----")
         print ("DISPOSITIVO REGISTRADO")
         print ("--- ---")
         print("Marca", self.marca)
         print("Modelo:", self.modelo)
         print("Año: ", self.año)
         print("Capacidade de la bateria: ", self.capacidad_bateria)

class Smartphone (Dispositivo): #subclase Carro
    #constructor
    def __init__(self, marca, modelo, año):
      super().__init__(marca, modelo, año) #super clase heredada
      self.sistema_operativo =  input("El sistema operativo de su smartphone es:")
      self.conectividad = input("El tipo de conectividad que maneja su smarphone es: ")
      self.bateria = input("Carga del celular es: ")
    #metodo privado
    def enceder(self):
        print("Sistema operetivo: ", self.sistema_operativo)
        print("Conectividad: ", self.conectividad) #impriendo La placa
        if  self.capacidad_bateria == 0:
         print ("----------------------")
         print(f"El smartphone {self.marca} modelo {self.modelo}, del año {self.año} La carga de su celular es {self.bateria} su dispositivo apagado !!")
        else:
         print ("----------------------")
         print(f"El smartphone {self.marca} modelo {self.modelo}, del  año {self.año} La carga de su celular es {self.bateria} su dipositivo encendido ")


#Instanciando La subclase 
objeto_Smartphone = Smartphone('Iphone', '16', '2024')
objeto_Smartphone.registrar() #registrando  
objeto_Smartphone.enceder() #encendiendo 
