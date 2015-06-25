#!/usr/bin/python

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

def gato():
	print '#'

def pon(casilla, item, gato):
	print casilla

def cambia(turno, item):
	turno, item

def gato_con_espacios():
	
linea= [[1,2,3],[4,5,6,],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

opc = raw_input('Elije una opcion (o/x)') #lee algo de teclado

# Un = es para asignacion, y == es para verificar
if opc=='o':
	turno='Player1'
	item='o'

else:
	turno='Player2'
	item='o'
print 'Es el turno de '+turno+' con: ' + item
win=False

while win==True:
	gato
	casilla= raw_input('Elije una casilla '+turno+ '(1-9)')
	cassilla= int(casilla)
	pon(cassilla, item, gato)
	if linea(casilla, gato):
		print 'Ganaste'
		win=True
	if gato_con_espacios():
		cambia(turno, item)
        print 'Gana Gato'
	win=True
print 'Fin del juego'
