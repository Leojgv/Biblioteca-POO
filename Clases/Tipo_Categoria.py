class Tipo_Categoria():
    #Clase que representa un tipo de categoría.
    #Tiene dos atributos: id_tipo_categoria (número) y tipo_categoria (string).

    def __init__(self, id_tipo_categoria, tipo_categoria):
        #Crea un tipo de categoría con su id y descripción.
        self.id_tipo_categoria = id_tipo_categoria
        self.tipo_categoria = tipo_categoria
