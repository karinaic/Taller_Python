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

############################################################################

#DIRECTORIOS

'''Para abrir archivos en una ruta de acceso distinta, importaremos el objeto:Path  y Os'''

import os

ruta = os.getcwd()  #este metodo nos da la ruta absoluta al archivo en el que estoy trabajando.
print(ruta)


ruta_1 = os.chdir('C:\\Users\\Karina\\Desktop\\alternativo')  #para abrir archivos que se encuentran en otro lugar, ponemos una ruta distinta

archivo = open('otro_archivo.txt') #abrimos el contenido de este archivo desde una carpeta distinta
print(archivo.read())


print(ruta_1)

#para crear una carpeta nueva

ruta_2 = os.makedirs('C:\\Users\\Karina\\Desktop\\alternativo\\otra')

###############################################################################

import os
#usando el metodo basename() puedo obteber el nombre base del archivo que intento abrir
# una ruta completa se compone de ruta al archivo + nombre del archivo

ruta = 'C:\\Users\\Karina\\Desktop\\alternativo\\prueba.txt'

elemento = os.path.basename(ruta)

print(elemento)

#si lo que queremos obtener el primer elemento hasta nuestro archivo, el nombre del directorio.
elemento_1 = os.path.dirname(ruta)

print(elemento_1)

#para ELIMINAR carpetas:
os.rmdir('RUTA HASTA LO QUE QUEREMOS ELIMINAR')


##################################################################################

from pathlib import Path
#de esta forma cualquier sistema operativo ya sea mac o windows va poder abrir este archivo.
carpeta = Path('C:/Users/Karina/Desktop/python_udemy/seccion_6')

archivo = carpeta / 'prueba.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

######Pathlib ####################

carpeta = Path('C:/Users/Karina/Desktop/python_udemy/seccion_6/prueba.txt')
print(carpeta.read_text())  #con este metodo leemos directamente el archivo, no hace falta abrir ni cerrar el archivo.


print(carpeta.name) #devuelve el nombre del archivo

print(carpeta.suffix) #nos devuelve la terminacion del archivo

print(carpeta.stem)

if not carpeta.exists():
    print('este archivo no existe')

else:
    print('existe')

########################################
from pathlib import Path
#de esta forma cualquier sistema operativo ya sea mac o windows va poder abrir este archivo.
carpeta = Path('C:/Users/Karina/Desktop/python_udemy/seccion_6')

archivo = carpeta / 'prueba.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

######Pathlib ####################

carpeta = Path('C:/Users/Karina/Desktop/python_udemy/seccion_6/prueba.txt')
print(carpeta.read_text())  #con este metodo leemos directamente el archivo, no hace falta abrir ni cerrar el archivo.


print(carpeta.name) #devuelve el nombre del archivo

print(carpeta.suffix) #nos devuelve la terminacion del archivo

print(carpeta.stem)

############Path######################
#te puede ser útil para:
'''* crear o mover archivos  
   * enumerar archivos
   * crear rutas apropiadas basadas en strings'''

# Ejemplo:  se va crear una ruta de acceso con todos estos strings como jerarquias de carpetas
mi_ruta = Path('europa', 'españa', 'barcelona', 'sagrada_familia.txt')
print(mi_ruta)  #se trataría de una ruta relativa

base = Path.home()
print(base)  # esto nos devuelve una ruta absoluta al directorio del usuario actual
guia = Path(base, 'Barcelona', 'Sagrada_familia.txt')
print(guia) #esto nos devuelve una ruta absoluta