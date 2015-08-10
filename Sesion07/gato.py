#!/usr/bin/python
#encoding:utf-8

#1.asignamos las variables
#2.leemos las opcion selecccionada
#3.la opcion es igual a o
#4.	si la opcion es igual entonces turno=P1 e item=o
#5.	si la opcion No es igual, entoncces turno=P2, item=o
#6.El juego termino?
#7.	si el juego No ha terminado Imprime el Gato
#8. 	"Escoje una casilla valida"
#9. 	Pon item en la casilla selecionada
#10. 	Hay 3 de item en linea?	
#11.		si hay 3 en linea "Ganaste"
#12.		termina=ganaste
#13.		Si hay espacios en gato
#14. 			cambiamos el turno y el item
#15. 		Si No hay espacios en gato
#16.			"Gana gato"
#17.			win=True			
#18.Regresa a 6
#19.si el juego termino finaliza
###############################################################################

# Hola Gato!

def tablero_gato(gato):
	'''
		¿que hace? Imprime el tablero
	'''
	print gato

def pon(item, casilla, gato):
	'''
		Pone el item en la casilla seleccionada del gato
	'''	
	if casilla in gato:
		i= gato.index(casilla) #revisa que casilla este en gato
		gato= gato[:i]+item+gato[i+1:]
	return gato

def cambia(turno, item):
	'''
		cambia  el turno dej jugador asi como su ficha
	'''
	if turno=='Player1' and item=='o':
		turno='Player2'
		item='x'
	elif turno=='Player2' and item=='x':
		turno='Player1'
		item='o'
	if turno=='Player2' and item=='o':
		turno='Player1'
		item='x'
	elif turno=='Player1' and item=='x':
		turno='Player2'
		item='o'

	return turno, item


def gato_con_espacios():
	'''
		Verifica que halla algun espacio disponible para tirar en el tablero_gato
	'''
	gato.replace('\n', '')
	new_gato= list(gato.replace('\n', ''))
	for casilla in new_gato:
		if casilla.isdigit():
			return True
	print 'No hay espacios'
	return False

def linea_win(casilla, item, gato):
	'''
		verifica quee  se forme un 3 en raya en base a la casilla	
	'''		
	linea= [[1,2,3],[4,5,6,],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
	new_gato= gato.replace('\n', '|').split('|')
	
	for raya in linea: #raya =[1,2,3]
		# ejempl de contenido_raya = ['x','2','o']
		contenido_raya = [new_gato[raya[0]-1], new_gato[raya[1]-1], new_gato[raya[2]-1]]
		if item in contenido_raya: # 'x' in ['x','2','o']?  
			#print item, raya
			cont=0
			for i in raya:	#i=(1-3), i=3
				if new_gato[i-1] == item:
					cont+=1
					#print cont
					if cont==3:
						# si es igual a 3 hay 3 en raya
						return True
						
	return False
					
#elemtos de listas				 
############ Define variables##################
gato='1|2|3\n4|5|6\n7|8|9'
new_gato= gato.replace('\n', '|').split('|') 

# new_gato = a la lista de elemntos en gato, sin tomar en cuenta \n
########################################################

opc = raw_input('Elije una opcion (o/x)') #lee algo de teclado y lo asigna a opc

# Un = es para asignacion, y == es para verificar
if opc=='o':
	turno='Player1'
	item='o'

else:
	turno='Player2'
	item='o'
print 'Es el turno de '+turno+' con: ' + item
win=False


while win==False: # while not win:
	tablero_gato(gato)	
	casilla= raw_input('Elije una casilla '+turno+ '(1-9): ')
	print	
	if casilla in gato:
		gato= pon(item, casilla, gato)
	
		if linea_win(casilla, item, gato):
			print 'Ganaste '+turno
			win=True
		if gato_con_espacios():
			turno, item = cambia(turno, item)
		else:
			win=True
	else: 
		print 'Dame otra casilla'
print 'Fin del juego'
