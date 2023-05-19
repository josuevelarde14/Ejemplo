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

class empleado(persona):
    def __init__(self, nombre, edad, telefono, salario, puesto):
        persona.__init__(self, nombre, edad, telefono)
        self.__salario = salario
        self.__puesto = puesto

    def getSalario(self):
            print(f"Mi salario es: {self.__salario}")

    def getPuesto(self):
            print(f"Mi puesto es: {self.__puesto}")

empleado1 = empleado("Josue",24,"986762755",9000,"Analista de datos")
empleado1.getNombre()
empleado1.getEdad()
empleado1.getTelefono()
empleado1.getPuesto()
empleado1.getSalario()
