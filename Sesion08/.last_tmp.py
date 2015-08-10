#!/usr/bin/python
#-*- coding: utf-8 -*-

#1. Deberá de leer un número que indica el número del campo a imprimir
#2. Deberá leer el archivo reporte.csv
#3. Deberá de imprimir el campo elegido al principio para todos los registros del archivo.
#4. Deberá imprimir los registros ordenados


# 1. Leer TODO el archivo reporte.csv y guardar su contenido en reporteread

# 2. Separar el contenido de reporter por líneas y guardar el resultado en reportelineas

# 3. Acomodar reportelineas por orden alfabetico 

# 4. 

# 3. Para cada línea en reportelineas hacer lo siguiente:

# 3.1. Separa la linea en base a los ":" y guardar en resultado en lineapuntos

# 3.2. Tomar el primer elemento de lineapuntos y guardarlo en primero

# 3.3. Imprimir primero


reporteopen=open("reporte.csv","r")
reporter=reporteopen.read() #usaremos este para modifcar el archivo
reporteopen.close()

reportelineas=reporter.split('\n')
reportelineas.sort()

for linea in reportelineas:
	lineasin=linea.split('""',',')
	
	i=raw_input("escoje una linea")
	i=int(i)
	num=lineasin[i]
	print num