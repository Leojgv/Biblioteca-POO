import Libro
import Editorial

class Detalle_Libro(Libro, Editorial):
    #Representa un libro en especifico dentro de la biblioteca
    def __init__(self, id_detalle_libro, isbn, fecha_edicion, id_editorial, numero_paginas, id_categoria_libro, cantidad_ejemplares, ejemplares_disponibles):
        #Crea un objeto que representa un libro en especifico dentro de la biblioteca. 
        Libro.__init__(isbn)
        Editorial.__init__(id_editorial)
        self.id_detalle_libro = id_detalle_libro
        self.fecha_edicion = fecha_edicion
        self.numero_paginas = numero_paginas
        self.id_categoria_libro = id_categoria_libro
        self.cantidad_ejemplares = cantidad_ejemplares
        self.ejemplares_disponibles = ejemplares_disponibles

    def actualizar_disponibilidad(self, origen, cantidad):        
        #Actualiza la cantidad de ejemplares disponibles en la biblioteca segun sea si se retira o se devuelve un libro.
        if(self.cantidad_ejemplares > self.ejemplares_disponibles + cantidad):
            if(origen == "retirar"):
                if(self.ejemplares_disponibles > 0):
                    self.ejemplares_disponibles = self.ejemplares_disponibles - cantidad
                else:
                    print("No hay ejemplares disponibles para realizar el préstamo.")
            else:
                self.ejemplares_disponibles = self.ejemplares_disponibles + cantidad
        else:
            print("Nuestros registros indican que hay un error en la cantidad de ejemplares.")
