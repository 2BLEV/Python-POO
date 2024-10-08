class Electronico:
    #constructor
    def __init__(self, marca, modelo, procesador):
      self.marca = marca
      self.modelo = modelo
      self.procesador = procesador
      self.memoria = int(input("¿Que cantidad de memoria ram tiene laptop?:"))
    
    #metodos público
    def registrar(self):
         print ("---- ----")
         print ("ELECTRONICO REGISTRADO")
         print ("--- ---")
         print("marca", self.marca)
         print("modelo:", self.modelo)
         print("procesador: ", self.procesador)
        

class Laptop (Electronico): #subclase Carro
    #constructor
    def __init__(self, marca, modelo, procesador):
      super().__init__(marca, modelo, procesador) #super clase heredada
      self.disco_duro =  input("¿Que tipo de discoduro tiene su laptop?:")
      self.bateria = input("¿Cuanto tiempo demora la bateria en horas?: ")
      
    #metodo privado
    def tocar(self):
        print("Su discuduro es : ", self.disco_duro)
        print("La duracion de su bateria son: ", self.bateria, "Horas") #impriendo La placa
        print("LAPTOP ENCENDIDAD")
       

#Instanciando La subclase 
objeto_Laptop = Laptop('HP', '2024', 'INTEL')
objeto_Laptop.registrar() #registrando  
objeto_Laptop.tocar() #encendiendo 