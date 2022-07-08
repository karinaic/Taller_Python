#Tareas fundamentales para abrir,cerrar y leer archivos en python
#utilizaremos metodos como : open(), write(), read() y close().

##Ejemplo. alojamos nuestro archivo en una variable
# mi archivo = open('archivo.txt') -->le pasamos el nombre del archivo entre comillas

mi_archivo = open('prueba.txt')
print(mi_archivo.read())

#metodo readline()-->lo que hace es leer solo unalinea

print(mi_archivo.readline())

una_linea = mi_archivo.readline()
print(una_linea)

#una linea al ser string podemos aplicarle todos los métodos conocidos para string.

# ejemplo:

print(una_linea.upper())

todas = mi_archivo.readlines()  #nos devuelve cada linea dentro de una lista.
print(todas)

# Ahora vamos a ver como hacer para generar cambios en el archivo original.
#mi_archivo = open(archivo.txt,'r' -> solo lectura)
#mi_archivo = open(archivo.txt,'w' ->solo escritura)
#mi_archivo = open(archivo.txt,'a' -> solo escritura posicionando al final del archivo, se crea el archivo si no existiera
#pero en el caso que existiera el archivo, el cursos se posicionaria al final para poder escribir a partir
# de ese lugar)
#Ejemplo:
#archivo = open('prueba.txt','r')
#archivo.write('soy el nuevo texto') #--> esto no funcionaria, porque lo hemos abierto con el metodo 'solo lectura'.

archivo = open('prueba1.txt','w')
archivo.write('soy el nuevo texto')

archivo.close()

#para agregar texto a nuestro archivo al final,como por ejemplo logs de un programa.

archivo = open('prueba1.txt','a')
archivo.write('Bienvenido')

archivo.close()

