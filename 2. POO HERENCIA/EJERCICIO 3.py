class Instrumento:
    #constructor
    def __init__(self, tipo, marca, material):
      self.tipo = tipo
      self.marca = marca
      self.material = material
    
    #metodos público
    def registrar(self):
         print ("---- ----")
         print ("INSTRUMENTO REGISTRADO")
         print ("--- ---")
         print("tipo", self.tipo)
         print("marca:", self.marca)
         print("material: ", self.material)
        

class Guitarra (Instrumento): #subclase Carro
    #constructor
    def __init__(self, tipo, marca, material):
      super().__init__(tipo, marca, material) #super clase heredada
      self.cuerdas =  input("Numero de cuerdas:")
      self.acordes = input("¿Que acordes basicos conoces?: ").split(",")
      
    #metodo privado
    def tocar(self):
        print("Numenro de cuerdas: ", self.cuerdas)
        print("TOCAR GUITARRA: ", self.acordes) #impriendo La placa
       

#Instanciando La subclase 
objeto_Guitarra = Guitarra('Guitarra', 'Española', 'madera')
objeto_Guitarra.registrar() #registrando  
objeto_Guitarra.tocar() #encendiendo 
