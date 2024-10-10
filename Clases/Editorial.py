import re

class Editorial():
    #Clase que representa una editorial. Tiene un id, nombre, fecha de fundacion, codigo de pais, telefono de contacto y correo electronico de contacto.
    def __init__(self, id_editorial, nombre_editorial, fecha_fundacion, codigo_pais, telefono_contacto, correo_contacto):
        # Inicializa una instancia de la clase Editorial.
        self.id_editorial = id_editorial
        self.nombre_editorial = nombre_editorial
        self.fecha_fundacion = fecha_fundacion
        self.codigo_pais = codigo_pais
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto

    def validar_correo(self):
        #Valida si el correo electronico tiene el formato correcto.
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, self.correo_contacto)):
            return True 
        else:
            return False
