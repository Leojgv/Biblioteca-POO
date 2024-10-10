import autor

class Libro(autor.Autor):
    #Representa un libro con su ISBN y titulo
    def __init__(self, isbn, titulo, id_autor):
        #Inicializa un libro con su ISBN, titulo y autor
        super().__init__(id_autor)
        self.isbn = isbn
        self.titulo = titulo
    
    def validar_isbn(self):
        #Valida si el ISBN es correcto (10-13 digitos)
        if(10 <= len(self.isbn) <= 13 and self.isbn.isdigit()):
            return True
        else:
            return False

        