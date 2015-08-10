#!/usr/bin/python
# -*- coding: utf-8 -*-

# Este programa toma el archivo passwd, lo lee linea a linea y luego imprime
# el primer campo de cada línea

# seudo código
#


# 1. Leer TODO el archivo passwd y guardar su contenido en passwdmem

# 2. Separar el contenido de passwdmem por líneas y guardar el resultado en passwdlineas

# 3. Para cada línea en passwdlineas hacer lo siguiente:

# 3.1. Separa la linea en base a los ":" y guardar en resultado en lineapuntos

# 3.2. Tomar el primer elemento de lineapuntos y guardarlo en primero

# 3.3. Imprimir primero

passwdopen=open("passwd","r")
passwd=passwdopen.read()
passwdopen.close()

passwdlineas=passwd.split('\n')
passwdlineas.sort()

for linea in passwdlineas:
	lineapuntos=linea.split(':')
	primero=lineapuntos[0]
	print primero


