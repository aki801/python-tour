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

# La siguiente línea no es necesaria ya que np ya es entero
# E=int(np) # convierte np a entero ¿cuanto vale np? A esta altura no se sabe

# La siguiente línea que hace? o para qué?
lp = list(P)

# Se crea una cadena con espacios de la misma longitud de la
# palabra seleccionada
Esp = "_"*np

# dead tiene cada uno de los estados de la muerte del monito
dead = [" O \n   \n   \n  \n"," O \n/  \n   \n   \n"," O \n/| \n   \n   \n"," O \n/|\\\n   \n   \n"," O \n/|\\\n |\n   \n"," O \n/|\\\n |\n/  \n"," O \n/|\\\n |\n/ \\\n"," O \n/|\\\n |\n/ \\\n"]

# I es la longitud de dead y es el número máximo de intentos que tiene
# el usuario para adivinar la palabra
I = len(dead)

# La siguiente línea me parece que no tiene uso y sentido, así que la comento
# dead=str()

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
print 'Intenta una letra'
L = raw_input() #lee algo de teclado
if L in P: # revisa si existe la letra en la palabra
  # si existe, entonces hay que buscar en que posición o posiciones
  # está la letra en toda la palabra, así que hay que recorrerla toda
  i=0
  while i<np:
    if L == P[i]: # si la letra L está ne la posición i
      # entonces hay que remplazarla en la variable de espacios
      Esp[i] = L
    i+=1
else:
  intentos+=1
  