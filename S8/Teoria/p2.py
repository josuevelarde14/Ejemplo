archivo=open("./S8/Teoria/datos.txt","w") #"r" para leer


archivo.write("6    zanahoria\n")
archivo.write("7    fideos\n")
archivo.write("8    camote\n")

archivo.close()

archivo=open("./S8/Teoria/datos.txt","r")
contenido=archivo.read()
print(contenido)
archivo.close()

archivo=open("./S8/Teoria/datos.txt","a")
archivo.write("linea 9\n")
archivo.write("linea 8\n")
archivo.close()

archivo=open("./S8/Teoria/datos.txt","r")
contenido=archivo.read()
print(contenido)
archivo.close()