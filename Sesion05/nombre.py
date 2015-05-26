#!/usr/bin/python

name= raw_input ('Introduce tu nombre completo: ')
nl=len(name)
p=name.split()
np=len(p)

print 'hola'+name+'tu nombre tiene '+ str(nl) +'letras, incluyendo espacios, y tiene '+ str(np) + 'palabras'


