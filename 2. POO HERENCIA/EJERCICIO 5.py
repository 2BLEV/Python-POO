class Reloj:
    #constructor
    def __init__(self, marca, tipo, material):
      self.marca = marca
      self.tipo = tipo
      self.material = material
      self.precio = int(input("¿Cual es el precio del reloj?:"))
    
    #metodos público
    def registrar(self):
         print ("---- ----")
         print ("RELOJ REGISTRADO")
         print ("--- ---")
         print("Marca", self.marca)
         print("Tipo:", self.tipo)
         print("Material: ", self.material)
         print("Precio. ", self.precio)
        

class RelojInteligente (Reloj): #subclase Carro
    #constructor
    def __init__(self, marca, tipo, material):
      super().__init__(marca, tipo, material) #super clase heredada
      self.pantalla =  input("¿Que tipo de pantalla tiene su RelojInteligente?:")
      self.sistema_operativo = input("¿Que tipi de sistema operativo tiene?: ")
      
    #metodo privado
    def tocar(self):
        print("Su discuduro es : ", self.pantalla)
        print("La duracion de su bateria son: ", self.sistema_operativo, "Horas") #impriendo La placa
        print("RelojInteligente ENCENDIDAD")
       

#Instanciando La fsubclase 
objeto_RelojInteligente = RelojInteligente('Samsung', 'Deportivo', 'PLASTICO')
objeto_RelojInteligente.registrar() #registrando  
objeto_RelojInteligente.tocar() #encendiendo 