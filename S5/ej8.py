class libro:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def getTitulo(self):
        print(f"El titulo del libro es: {self.__titulo}")
    def getAutor(self):
        print(f"El autor del libro es: {self.__autor}")
    def getPaginas(self):
        print(f"El libro tiene: {self.__paginas} páginas")
    
libro1 = libro("Kybalión","William Walker Atkinson","160")
libro1.getTitulo()
libro1.getAutor()
libro1.getPaginas()

