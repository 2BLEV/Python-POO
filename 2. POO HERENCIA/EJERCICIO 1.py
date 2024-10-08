class Electrodomestico:
    #constructor
    def __init__(self, marca, color, capacidad):
      self.marca = marca
      self.color = color
      self.capacidad = capacidad
      self.consumo_electrico = int(input("Consumo electrico en KWh:"))
    #metodos público
    def registrar(self):
         print ("---- ----")
         print ("ELECTRODOMESTICO REGISTRADO")
         print ("--- ---")
         print("Marca", self.marca)
         print("Color:", self.color)
         print("Capacidad: ", self.capacidad)
         print("Consumo electrico: ", self.consumo_electrico)

class Refrigerador (Electrodomestico): #subclase Carro
    #constructor
    def __init__(self, marca, color, capacidad):
      super().__init__(marca, color, capacidad) #super clase heredada
      self.tipo =  input("El tipo de nevera es:")
      self.temperatura = int(input("La temperatura incial en grados centigrados es: "))
    #metodo privado
    def ajustar(self):
        print("Tipo: ", self.tipo) #impriendo La placa
        if  self.temperatura > 0:
         print ("----------------------")
         print(f"El refrigerador {self.marca} de color {self.color}, con capacidade de {self.capacidad} temperatura esta alta se ajusto a 0°C !!")
        else:
         print ("----------------------")
         print(f"El refrigerador {self.marca} de color {self.color}, con capacidad de {self.capacidad} temperatura controlada")


#Instanciando La subclase 
objeto_refrigerador = Refrigerador('HACEB', 'GRIS', '150 L')
objeto_refrigerador.registrar() #registrando  
objeto_refrigerador.ajustar() #encendiendo 

