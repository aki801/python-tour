#!/usr/bin/python
#-*- coding: utf-8 -*-

#1. Deberá de leer un número que indica el número del campo a imprimir (validar si en campo a imprimir est dentro del archivo)
#2. Deberá leer el archivo reporte.csv
#3. Deberá de imprimir el campo elegido al principio para todos los registros del archivo.
#4. Deberá imprimir los registros ordenados


# 1. Leer TODO el archivo reporte.csv y guardar su contenido en reporteread

# 2. Identificar las , que son separadores y las que estan dentro de las cadenas

# 2. Separar el contenido de reporter por líneas y guardar el resultado en reportelineas

# 3. Acomodar reportelineas por orden alfabetico 

# 3. Para cada línea en reportelineas hacer lo siguiente:

# 3.1. Separa la linea en base a los ":" y guardar en resultado en lineapuntos

# 3.2. Tomar el primer elemento de lineapuntos y guardarlo en primero

# 3.3. Imprimir primero


reporteopen=open("reporte.csv","r")
reporter=reporteopen.read() #usaremos este para modifcar el archivo
reporteopen.close()

reporteam=reporter.replace('","','"&"')#reemplaza las comas que estan dentro de las comillas
reporteam=reporteam.replace(',,', '&&')#reemplaza las las 2 comas
reporteline=reporteam.split('\n')

i=raw_input("escoje un campo: ")
i=int(i)
i=i-1

for linea in reporteline:
	lineasin=linea.split('&')
	print len(lineasin)
	print linea
	print 
	print lineasin[i]
