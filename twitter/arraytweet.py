#!/usr/bin/python
## -*- coding: UTF-8 -*-

from twitter import *
import random #para # al azar

#los access y consumer los obenemos de twitter
access_token='793851762-n5g6OOTHPcnlKbfPdIK71svZ1a1ydgzbVRKeU0iR'
access_token_secret='7ppuW249zibj0BKCwBkw8LvUxaKzzdYjzdmlFRYO9w6SC'
consumer_key='XZ6cKayf2OhmTWHkdODJarYPj'
consumer_secret='rkMPWIunDY1QJyQfX8Z4MhJ3nklnzoYONjUvsA9lIJSiWVCAFY'

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

#parar ver los 2 ultimos tweets
#x = t.statuses.home_timeline(count=2)
#print x

frases= ["Hoy es un dia genias", "probando arrays", "tweet unsando arrays", "Esto es una prueba"]
#frace= len(fraces)
#num= random.randint(0,frace)
#mensaje=frases[num]
x= random.choice(frases)

#para actualizar estado en twitter
t.statuses.update(status=x)
