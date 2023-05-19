import os
class Agenda:
    def __init__(self):
        self.tareas = []

    def menu_opciones(self):
        os.system ("cls")
        print("Ingresa una opción")
        print(" 0: Salir de la agenda")
        print(" 1: Crear nueva tarea")
        print(" 2: Lista todas las tareas")
        print(" 3: Elminar una tarea")
        cadena = input()
        opt = -1
        if len(cadena)!=0:
            opt = int(cadena)
        return opt
    
    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)

        
