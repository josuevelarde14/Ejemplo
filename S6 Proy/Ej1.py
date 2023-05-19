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

    def nueva_tarea(self):
        descripcion = input("Ingresa una descripción: ")
        vencimiento = input("Ingresa una fecha de vencimiento: ")
        self.agregar_tarea(Tarea(descripcion,vencimiento))

    def listar_tareas(self):
        os.system ("cls")
        i = i
        for tarea in self.tareas:
            print(f"Tarea N° {i}")
            i += 1
            tarea.imprimir_informacion()
        input("\npresiona una tecla para continuar...")

    def eliminar_tarea(self):
        descripcion_tarea = input("Ingresa la descripcion de la tarea a eliminar")
        remove = False
        for tarea in self.tareas:
            if tarea.descripcion == descripcion_tareas:
                self.tareas.remove(tarea)
                remove = True
        if remove:
            print(f"Tarea {descripcion_tarea} eliminada correctamente")
        else:
            print(f"no existe la tarea {descripcion_tarea}")
        input("\npresiona una tecla para continuar...")
    
class Tarea:
        def __init__(self, descripcion, fecha_vencimiento):
            self.descripcion = descripcion
            self.fecha_vencimiento = fecha_vencimiento

        def imprimir_informacion(self):
            print(f"    -descripción: {self.descripcion}" )
            print(f"    -Fecha de vencimiento: {self.fecha_vencimiento}")

mi_agenda = Agenda()
mi_tarea1 = Tarea("Hacer las compras","10/05/2023")
mi_tarea2 = Tarea("Cocinar algo rico","12/05/2023")

mi_agenda.agregar_tarea(mi_tarea1)
mi_agenda.agregar_tarea(mi_tarea2)

while True:
    opcion = mi_agenda.menu_opciones()

    if opcion == 0:
        os.system ("cls")
        print(f"Vuelve pronto!!")
        break
    elif opcion == 1:
        mi_agenda.nueva_tarea()
    elif opcion == 2:
        mi_agenda.listar_tareas()
    elif opcion == 3:
        mi_agenda.eliminar_tarea()
    else:
        print(f"Esta opcion no se encuentra disponible, intenta de nuevo")




