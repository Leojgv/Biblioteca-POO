import Libro

class Biblioteca():
    #Clase que representa una biblioteca.
    def __init__(self, id_biblioteca, nombre_biblioteca, direccion_biblioteca, telefono_biblioteca):
        #Constructor de la clase Biblioteca.
        self.id_biblioteca = id_biblioteca
        self.nombre_biblioteca = nombre_biblioteca
        self.direccion_biblioteca = direccion_biblioteca
        self.telefono_biblioteca = telefono_biblioteca
    
    def buscar_libro(self, identificacion):
        #Busca un libro por su identificacion.
        pass
    
    def prestar_libro(self):
        #Presta un libro.
        pass
    
    def devolver_libro(self):
        #Devuelve un libro.
        pass
