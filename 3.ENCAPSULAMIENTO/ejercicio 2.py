#Clase Productos con atributos encapsulados o privados
class Productos:
    #metodo constructor
    def __init__(self, nombres, precio, cantidad, categoria):
        self.__nombres = nombres #privado
        self.__precio = precio #privado
        self.cantidad = cantidad #publico
        self.categoria = categoria #público
    

    #metodo getter
    def obtener_nombres(self):
        return self.__nombres

    #metodo getter
    def obtener_precio(self):
        return self.__precio

    #metodo setter
    def establecer_nombres(self, nuevo_nombres):
        self.__nombres = nuevo_nombres

    #metodo setter
    def establecer_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    #metodo mostrar detalles del objeto    def mostrar_detalles(self):
    def mostrar_detalles(self):
        print(f"\nNombres: {self.__nombres}")
        print(f"precio: {self.__precio}")
        print(f"cantidad: {self.cantidad}")
        print(f"Categoria: {self.categoria}")
    

#objeto
producto = Productos("Jorge", 20000, 5, "alimentos")

#imprimir atributos publicos y privados
producto.mostrar_detalles()

print("--------------------------")

#imprimir el atributo encapsulado modificando su acceso con getter y setter
producto.establecer_nombres("Carlos") #setter
print(f"Nombres: {producto.obtener_nombres()}") #getter
producto.establecer_precio(30000) #setter
print(f"precio: {producto.obtener_precio()}") #getter
print(f"No cantidad: {producto.cantidad}") #publico
print(f"Categoria: {producto.categoria}") #público

