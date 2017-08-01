#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Dado un verso con las posibles sinalefas marcadas, junto a el número de sinalefas que DEBE resolver y el número de sinalefas que PUEDE resolver, calcular todas las posibles combinaciones y las resuelve todas.

#Los patrones métrico posibles se calculan mediante combinaciones sin repetición. PR (sinalefas que se pueden resolver) es el número de elementos a agrupar. DR (sinalefas que se deben resolver) es el número de agrupaciones que se pueden hacer. La cantidad de patrones métrico posibles es por tanto el número de combinaciones sin repetición entre DR y PR: c=DR!/PR!(DR-PR)!
#Importate: el número de posibilidades (PR) debe ser siempre superior al número de sinalefas necesarias (DR).

#30 de octubre de 2015
#Borja Navarro Colorado
#Universidad de Alicante


import re
from itertools import combinations

def resuelveAmbiguas(verso, DR, PR):
	'Dado un verso métricamente ambiguo, resuelve todas las posibles agrupaciones métricas. El verso debe tener ya marcadas las separaciones silábicas donde se podría realizar sinalefa.'
		
	#1. Cambiamos marcas a números.
	n=1
	verso_num = ''
	for item in verso:
		if item != '#':
			verso_num += item
		elif item == '#':
			verso_num += '#'+str(n)+'#'
			n+=1

	#2. Generamos las posibles combinaciones de números.
	num = ''
	for i in range(1,PR+1):
		num+=str(i)
	
	#3. Resolvemos
	versosAmbiguos_resueltos = []
	combinaciones = combinations(num, DR)
	for combinacion in combinaciones:
		v = verso_num
		for item in combinacion:
			v = re.sub('#'+item+'#-', '', v) #Resuelve sinalefa: quita marcas y separador silábico.
		salida = ''
		salida = re.sub('#.#', '', v) #No resuelve sinalefa: quita marcas pero no quita el separador silábico.
		versosAmbiguos_resueltos.append(salida)
	
	return versosAmbiguos_resueltos #Atención: devuelve una lista, no cadena.
		
		
