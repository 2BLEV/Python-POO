#Clase Libro con atributos encapsulados o privados
class Libro:
    #metodo constructor
    def __init__(self, titulo, autor, isbn, editorial):
        self.__titulo = titulo #privado
        self.__autor = autor #privado
        self.__isbn = isbn #privado
        self.editorial = editorial #público
     

    #metodo getter
    def obtener_titulo(self):
        return self.__titulo

    #metodo getter
    def obtener_autor(self):
        return self.__autor

    #metodo getter
    def obtener_isbn(self):
        return self.__isbn

    #metodo setter
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    #metodo setter
    def establecer_autor(self, nuevo_autor):
        self.__autor = nuevo_autor
        
    #metodo setter
    def establecer_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn

    #metodo mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\ntitulo: {self.__titulo}")
        print(f"autor: {self.__autor}")
        print(f"No isbn: {self.__isbn}")
        print(f"Editorial: {self.editorial}")


#objeto
persona = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 9788497592208, "Sudamericana")

#imprimir atributos publicos y privados
persona.mostrar_detalles()

print("--------------------------")

#imprimir el atributo encapsulado modificando su acceso con getter y setter
persona.establecer_titulo("Mientras llueve") #setter
print(f"titulo: {persona.obtener_titulo()}") #getter
persona.establecer_autor("Fernando Soto Aparicio") #setter
print(f"autor: {persona.obtener_autor()}") #getter
persona.establecer_isbn(9789583002823) #setter
print(f"No isbn: {persona.obtener_isbn()}") #getter
print(f"Fecha nacimiento: {persona.editorial}") #público

