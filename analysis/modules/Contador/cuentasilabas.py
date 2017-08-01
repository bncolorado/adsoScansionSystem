#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Cuenta las sílabas. Calcula +/- 1 según última sílaba.

#29 de octurbe de 2015
#Borja Navarro Colorado
#Universida de Alicante

import string

def cuentasilabas(verso_bruto):
	'Cuenta las sílabas de un verso, previamente separadas por guión o espacio en blanco, y suma o resta según la última palabra sea aguda, llana o estrújula.'

	#1. Cuenta las sílabas
	verso = []
	[verso.append(item) for item in verso_bruto.split() if item not in u',;.:!?¡¿ '] #Aseguramos que no hay signos de puntuación ni espacio en blanco extra (podrían dar problemas al contador luego).
	contador = len(verso)
	for palabra in verso:
		for letra in palabra:
			if letra == '-':
				contador+=1

        #2. Compensación métrica: suma o resta el contador según sea aguda, llana o esdrújula
	palabrafin = verso[len(verso)-1]
	silabasPalabrafin = palabrafin.split('-')
	if len(silabasPalabrafin) >= 3:
        	if silabasPalabrafin[len(silabasPalabrafin)-1][0] in string.ascii_uppercase+u'Ñ':
        	        contador += 1
        	elif silabasPalabrafin[len(silabasPalabrafin)-2][0] in string.ascii_uppercase+u'Ñ':
        	        contador = contador
        	elif silabasPalabrafin[len(silabasPalabrafin)-3][0] in string.ascii_uppercase+u'Ñ':
        	        contador -= 1
	if len(silabasPalabrafin) == 2: #Si sólo tiene dos sílabas, no se mira la antepenúltima para evitar error de "out of index"
	        if silabasPalabrafin[len(silabasPalabrafin)-1][0] in string.ascii_uppercase+u'Ñ':
        	        contador += 1
	        elif silabasPalabrafin[len(silabasPalabrafin)-2][0] in string.ascii_uppercase+u'Ñ':
        	        contador = contador
	if len(silabasPalabrafin) == 1: #Si la última palabra es monosílaba y si es tónica el verso es agudo. Si no, se mira la antepenúltima.
		palabraAnteFin = verso[len(verso)-2]
		silabasPalabraAntefin= palabraAnteFin.split('-')
		if silabasPalabrafin[len(silabasPalabrafin)-1][0] in string.ascii_uppercase+u'Ñ':
		        contador += 1
		elif silabasPalabraAntefin[len(silabasPalabraAntefin)-1][0] in string.ascii_uppercase+u'Ñ':
		        contador = contador
		elif silabasPalabraAntefin[len(silabasPalabraAntefin)-2][0] in string.ascii_uppercase+u'Ñ':
		        contador -= 1

	return contador
