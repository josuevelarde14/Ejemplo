
archivo = open("./S8/Practica/ej5/datos.txt","r")
content = archivo.read()
words = content.split()
archivo.close()



archivoname = "my"
word_list = ""


lines = len(archivo.readlines())
print(lines)
archivo.close()

#Todo