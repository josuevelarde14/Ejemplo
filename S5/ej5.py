class persona:
    def __init__(self, nombre, edad, telefono):
        self.__nombre = nombre
        self.__edad = edad
        self.__telefono = telefono
        self.__datos = ""

    def getNombre(self):
        print(f"Mi nombre es: {self.__nombre}")

    def getEdad(self):
        print(f"Mi edad es: {self.__edad}")

    def getTelefono(self):
        print(f"Mi telefono es: {self.__telefono}")

persona1 = persona("Josue",24,"986762755")
persona1.getNombre()
persona1.getEdad()
persona1.getTelefono()
