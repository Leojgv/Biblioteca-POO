
import Paises
import Tipo_usuario
import re

class Usuario(Paises, Tipo_usuario):
    def __init__(self, id_usuario, nombre_usuario, correo_usuario, telefono_usuario, rut_usuario, codigo_pais, habilitado, id_tipo_usuario, fecha_creacion):
        Paises.__init__(codigo_pais)
        Tipo_usuario.__init__(id_tipo_usuario)
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.correo_usuario = correo_usuario
        self.telefono_usuario = telefono_usuario
        self.habilitado = habilitado
        self.fecha_creacion = fecha_creacion    
    
    def validar_correo(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, self.correo_usuario)):
            return True 
        else:
            return False
