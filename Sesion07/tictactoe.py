#!/usr/bin/python
# -*- coding: utf-8 -*-

# TicTacToe: Es un programa para jugar gato entre dos personas

def hay_espacios(tablero):
    '''
        Si hay espacios en tablero regresa verdadero, de lo
        contrario regresa falso
    '''
    if "-" in tablero:
        return True
    else:
        return False

def imprime_tablero(tablero):
    '''
        Imprime el tablero dado por tablero
    '''
    print
    for i in range(9):
        if i%3 == 0 and i>0:
            print
            print "-"*9
        elif i>0:
            print "|",
        if tablero[i] == '-':
            print i+1,
        else:
            print tablero[i],
    print
        
def lee_tirada(turno, tablero):
    '''
        Muestra un mensaje para el jugador en turno, lee y
        regresa el valor de la tirada elegida por el jugador
    '''
    resp_valida = False
    op = 0
    while not resp_valida:
        print
        print "Jugador "+str(turno+1)
        op = raw_input("Dame la posición de tu tirada (1-9)?")
        op = int(op)
        if op<1 or op>9 or tablero[op-1] != "-":
            print
            print "tirada inválida!"
            print
            imprime_tablero(tablero)
        else:
            resp_valida = True
    
    return op-1

def actualiza_tablero(tablero, tirada, turno, jugador):
    '''
        Actualiza el tablero con la tirada realizada para el
        jugador en turno
    '''
    tablero[tirada] = jugador[turno]

def gana(tirada, turno, tablero):
    '''
        Determina si el jugador en turno ha ganado
    '''
    gane = False
    hor = [
            [0,1,2],
            [3,4,5],
            [6,7,8]
          ]
    ver = [
        [0,3,6],
        [1,4,7],
        [2,5,8]
    ]
    dia = [
        [0,4,8],
        [2,4,6]
    ]
    # Vemos si es posible ganar en horizontal
    for linea in hor:
        if tirada in linea:
            # Se construlle la línea en base al tablero
            tlinea = []
            for n in linea:
                tlinea.append(tablero[n])
            # Se verifica si se ha ganado
            if "-" in tlinea:
                gane = False
            elif "x" in tlinea and "o" in tlinea:
                gane = False
            else:
                return True

    # Vemos si es posible ganar en vertical
    for linea in ver:
        if tirada in linea:
            # Se construlle la línea en base al tablero
            tlinea = []
            for n in linea:
                tlinea.append(tablero[n])
            # Se verifica si se ha ganado
            if "-" in tlinea:
                gane = False
            elif "x" in tlinea and "o" in tlinea:
                gane = False
            else:
                return True

    # Vemos si es posible ganar en diagonal
    for linea in dia:
        if tirada in linea:
            # Se construlle la línea en base al tablero
            tlinea = []
            for n in linea:
                tlinea.append(tablero[n])
            # Se verifica si se ha ganado
            if "-" in tlinea:
                gane = False
            elif "x" in tlinea and "o" in tlinea:
                gane = False
            else:
                return True

    return gane

# Bloque principal
tablero = ("- "*9).split()
jugador = ["",""]
op = raw_input("Jugador1 elige 'o' o 'x'? ")
if op == "o":
    jugador[0] = "o"
    jugador[1] = "x"
    turno = 0
else:
    jugador[0] = "x"
    jugador[1] = "o"
    turno = 1

imprime_tablero(tablero)
gano = False
while hay_espacios(tablero) and gano == False:
    tirada = lee_tirada(turno, tablero)
    actualiza_tablero(tablero, tirada, turno, jugador)
    imprime_tablero(tablero)
    if gana(tirada, turno, tablero):
        print
        print "El jugador "+str(turno+1)+" ha ganado!"
        print
        gano = True
    else:
        turno = (turno+1)%2

if not gano:
    print
    print "Gato!"
    print
