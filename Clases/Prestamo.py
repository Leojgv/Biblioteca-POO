from datetime import datetime, timedelta
from Auxiliares import constantes
import Detalle_Libro
import Usuario

class Prestamo(Detalle_Libro, Usuario):
    #Clase que representa un prestamo de un libro a un usuario.
    def __init__(self, id_prestamo, isbn, id_usuario, fecha_prestamo, fecha_devolucion, fecha_devuelto, cantidad_solicitada):
        # Inicializa un objeto de la clase Prestamo.
        Detalle_Libro.__init__(isbn)
        Usuario.__init__(id_usuario)
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_devuelto = fecha_devuelto
        self.cantidad_solicitada = cantidad_solicitada
    
    def sumar_dias_laborales(fecha_prestamo, dias_prestamo):
        # Suma los dias laborales a la fecha de prestamo
        dias_agregados = 0  
        while dias_agregados < dias_prestamo:
            fecha_prestamo += timedelta(days=1)
            if fecha_prestamo.weekday() < 5 and fecha_prestamo not in constantes.festivos:
                dias_agregados += 1
        return fecha_prestamo

    def calcular_fechas(self):
        # Si hay ejemplares disponibles, se asume como fecha de prestamo la fecha actual y se calcula la fecha de devolucion sumando 5 dias laborales
        if(self.ejemplares_disponibles > 0):
            if(self.ejemplares_disponibles > self.cantidad_solicitada):
                self.fecha_prestamo = datetime.datetime.now()
                self.fecha_devolucion = Prestamo.sumar_dias_laborales(self.fecha_prestamo, 5)
