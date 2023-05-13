archivo=open("./S8/Practica/ej4/datos.txt","r")  #"r" para leer

lines = len(archivo.readlines())
print(lines)
archivo.close()

