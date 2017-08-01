# -*- coding: utf-8 -*-

#Dado un verso separado en sílabas y con las sílabas tónicas (de las palabras métricamente tónicas) marcadas, cambia la representación a un patrón donde "+" representa sílaba tónica y "-" representa sílaba átona.

#7 de agosto de 2013 - 29 de octubre de 2015
#Borja Navarro Colorado
#Universidad de Alicante

import string

def extraepatron(verso):
	'Dado un verso separados por sílabas con guión, genera patrón métrico.'
	a = verso.replace(" ", "-") #separa todas las sílabas con guión.
	l = []
	[l.append(item) for item in a.split('-') if item != ''] #Aseguramos que no quedan sílabas vacías por espacios en blanco.
	salida = ''
	for i in l:
		item = i
		index=int(len(item)/2)
		if item[0] in string.ascii_uppercase or item[0] in [u'Ñ', u'Á', u'É', u'Í', u'Ó', u'Ú']: #Si la primera letra es mayúscula, la sílaba entera es tónica
         		salida += '+'
		elif item[len(item)-1] in string.ascii_uppercase or item[len(item)-1] in [u'Ñ', u'Á', u'É', u'Í', u'Ó', u'Ú']: #Si la última letra es mayúscula, la sílaba entera es tónica
        	 	salida += '+'
		elif item[index] in string.ascii_uppercase or item[index] in [u'Ñ', u'Á', u'É', u'Í', u'Ó', u'Ú']: #Si la letra central es mayúscula, la sílaba entera es tónica
        		salida += '+'
		elif item[0] in string.ascii_lowercase or item[0] in u'ñ': #Resto de casos (primera letra minúscula), sílaba átona
        		salida += '-'
		else:
        		print ('Error: sílaba sin signo alfabético. No se considera en patrón.') #Casos de signos de puntuación.

	if salida[-1] == '+': #Si el patrón es agudo, se añade una sílaba átona más.
		salida += '-'
	if salida[-2] == '-' and salida[-1] == '-':
		salida = salida[:-1] #Si el patrón es esdrújulo, se elimina la última sílaba átona.

	return salida

