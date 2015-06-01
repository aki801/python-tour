#!/usr/bin/python
#-*- coding: utf-8 -*-
# La línea anterior permite escribir acentos y ñ's dentro del código

import random #esto es para que funcione la función de aleatorio

# B es un diccionario de palabras
B = [
  "gato",
  "perro",
  "bandera",
  "ornitorrinco",
  "lampara",
  "anime",
  "espejo",
  "motocicleta",
  "television",
  "libreta"]

# Se elige una palabra al hazar del diccionario
P = random.choice(B)

# Se calula la longitud de la palabra seleccionada
np=len(P)

# La siguiente línea que hace? o para qué?
lp = list(P)

# Se crea una cadena con espacios de la misma longitud de la
# palabra seleccionada
Esp = "-"*np
Et= np
# dead tiene cada uno de los estados de la muerte del monito
dead = [" O \n   \n   \n  \n"," O \n/  \n   \n   \n"," O \n/| \n   \n   \n"," O \n/|\\\n   \n   \n"," O \n/|\\\n |\n   \n"," O \n/|\\\n |\n/  \n"," O \n/|\\\n |\n/ \\\n"," O \n/|\\\n |\n/ \\\n"]

# I es la longitud de dead y es el número máximo de intentos que tiene
# el usuario para adivinar la palabra
I = len(dead)

# horca contiene el ascii para puntar la horca y es un string, lo cambio!
horca = " +----+ \n |    | \n |      \n |      \n |      \n========"

# El número de intentos es:
intentos = 0

##############
# A partir de aquí todo el bloque de abajo debería de repetirse
# ¿cierto? ¿que tipo de ciclo podrías usar?
# Ya he creado la variable "intentos" con ella podrías definir hasta donde
# tiene que llegar el ciclo, pero sólo es una parte ¿qué falta?

print "Juguemos al ahorcado"
print horca
print Esp

while Et!=0 and intentos<I:
	print 'Intenta una letra'
	L = raw_input() #lee algo de teclado
	if L in P: # revisa si existe la letra en la palabra
		# si existe, entonces hay que buscar en que posición o posiciones
		# está la letra en toda la palabra, así que hay que recorrerla toda
		i=0
		while i<np:
			if L == P[i]: # si la letra L está np la posición i
		      	# entonces hay que remplazarla en la variable de espacios
				Esp= Esp[:i]+L+Esp[i+1:]
				Et= Et-1
			i+=1
		print Esp
	else:
		print dead[intentos]
		intentos+=1	
 
else:
	if intentos==I:
		print 'Perdiste'
	else:
		print 'Ganaste'
		
