class Cancion:
    def __init__(self, titulo, artista, album, duracion):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

class BibliotecaMusical:
    def __init__(self):
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def buscar_cancion(self, clave):
        for cancion in self.canciones:
            if clave in cancion.titulo or clave in cancion.artista or clave in cancion.album:
                print(f"{cancion.titulo} - {cancion.artista}")

    def crear_lista_reproduccion(self, nombre):
        lista_reproduccion = []
        for cancion in self.canciones:
            if nombre.lower() in cancion.titulo.lower() or nombre.lower() in cancion.artista.lower() or nombre.lower() in cancion.album.lower():
                lista_reproduccion.append(cancion)
        return lista_reproduccion

biblioteca_musical = BibliotecaMusical()

cancion1 = Cancion("La Prisión", "Rels B", "La Isla LP", "3:20")
cancion2 = Cancion("Hotel California", "Eagles", "Hotel California", "6:30")
cancion3 = Cancion("Imagine", "John Lennon", "Imagine", "3:04")
cancion4 = Cancion("Un Verano En Mallorca", "Rels B", "La Isla LP", "2:24")
cancion5 = Cancion("Dakiti", "Bad Bunny", "El último tour del mundo", "3:25")
cancion6 = Cancion("SIN MIRAR LAS SEÑALES", "Rels B", "Happy Birthday Flakko", "3:00")

biblioteca_musical.agregar_cancion(cancion1)
biblioteca_musical.agregar_cancion(cancion2)
biblioteca_musical.agregar_cancion(cancion3)
biblioteca_musical.agregar_cancion(cancion4)
biblioteca_musical.agregar_cancion(cancion5)
biblioteca_musical.agregar_cancion(cancion6)

biblioteca_musical.buscar_cancion("Bad Bunny")
biblioteca_musical.buscar_cancion("Imagine")

lista_reproduccion = biblioteca_musical.crear_lista_reproduccion("Rels B")
for cancion in lista_reproduccion:
    print(f"{cancion.titulo} - {cancion.artista}")

archivo=open("./Proyecto_1/Listadereproduccion.txt","w")
for cancion in lista_reproduccion:
    archivo.write(f"{cancion.titulo} - {cancion.artista}\n")
archivo.close()
