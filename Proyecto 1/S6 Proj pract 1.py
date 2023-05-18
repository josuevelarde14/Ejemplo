class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, clave):
        for libro in self.libros:
            if clave in libro.titulo or clave in libro.autor:
                print(f"{libro.titulo} de {libro.autor}")
    
    def prestar_libro(self, clave):
        for libro in self.libros:
            if clave in libro.titulo and libro.disponible:
                libro.disponible = False
                print(f"El libro {libro.titulo} ha sido prestado")
                return
        print("El libro no esta disponible")

    def devolver_libro(self, clave):
        for libro in self.libros:
            if clave in libro.titulo and not libro.disponible:
                libro.disponible = True
                print(f"El libro {libro.titulo} ha sido devuelto")
                return
        print("El libro no fue prestado o no se encuentra en la biblioteca")
        
biblioteca = Biblioteca()

libro1 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling")
libro2 = Libro("El principito", "Antoine de Saint-Exupéry")
libro3 = Libro("1984", "George Orwell")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

biblioteca.buscar_libro("El principito")
biblioteca.prestar_libro("1984")
biblioteca.devolver_libro("1984")