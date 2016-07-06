# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.
# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.
# The phrase turn on actually means that you should increase the brightness of those lights by 1.
# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
# The phrase toggle actually means that you should increase the brightness of those lights by 2.
# What is the total brightness of all lights combined after following Santa's instructions?
# For example:
# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.

#Answer: 14110788

import re

numbers = list()
w = 1000
h = 1000
matrix = [ [ 0 for x in range( w ) ] for y in range( h ) ]

def changelights( stri, lista ):
	for positiony, y in enumerate( matrix ):
		if positiony >= int( lista[1] ) and positiony <= int ( lista[3] ):
			for x in range(int( lista[0] ), int( lista[2] )+1):
				if stri == "on":
					y[x]+=1
				elif stri == "off":
					if y[x] is not 0:
						y[x] -= 1
				else:
					y[x]+=2

def count():
	cos = 0
	for y in matrix:
		for x in range(0,w):
			cos+=y[x]
	return cos

with open( "06 - Probably a Fire Hazard.txt" ) as txt:
	for line in txt:
		numbers = re.findall( '\d+', line )
		if line[ 1 ] == "u":
			if line[ 6 ] == "n":
				changelights( "on", numbers )
			else:
				changelights("off", numbers)
		else:
			changelights("toggle", numbers)

print(count())