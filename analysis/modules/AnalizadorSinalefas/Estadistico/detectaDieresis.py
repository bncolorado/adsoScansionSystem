#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Dado un verso con menos de once sílabas, separa los diptongos que podrían ser objeto de diéresis. No diferencia entre diéresis e hitato. Las reglas de separación se han realizado a mano (ver dieresis_reglas.py).
# Si el verso resultante tiene 11 sílabas o menos, lo analiza.
#Si tiene más de 11 sílabas, se llama al módulo de resolución por combinación.

#Borja Navarro Colorado
#Universidad de Alicante
#2015-2017

import re
from modules.AnalizadorSinalefas.Estadistico import dieresis_reglas
from modules.AnalizadorSinalefas.Estadistico import detectaSinalefa
from modules.Contador import cuentasilabas

def separaDieresis(verso):
	'Dado un verso con menos de 11 sílabas, separa aquéllas que tienen diptongo. Las reglas de separación se han hecho a mano. Ver la gramática en dieresis_reglas.py'
	verso = re.sub(' ','-',verso) #Se marcan todos los separados silábicos igual, sin diferenciar entre separación silábica o entre palabras.
	if verso[-1] == '-':
		verso = verso[:-1]
	if verso[0] == '-':
		verso = verso[1:]
	v = verso.split('-') #Lista con las sílabas del verso.

	c = 0
	salida = ''
	while c < len(v):
		silaba = v[c]
		s = dieresis_reglas.separadieresis(silaba)
		salida += s+'-'
		c+=1
	salida = salida[:-1]

	NumeroSilbas = cuentasilabas.cuentasilabas(salida)
	DR = NumeroSilbas-11

	return salida, DR

	
def detectaDieresis(verso, SinalefasDebeResolver):
	'Marca las sinalefas que se pueden resolver. Deteca si hay ambigüedad: si se pueden resolver más que las que DEBE resolver. Extrae todos los patrones posibles.'
	verso_separado, SinalefasDebeResolver = separaDieresis(verso)
	if SinalefasDebeResolver < 1: #No hay ambigüedad.
		return verso_separado
	else:
		print ('\tEjecuta resolución sinalefas. Hay al menos una por resolver.')
		verso_resuelto = detectaSinalefa.detectaSinalefas(verso_separado, SinalefasDebeResolver)
		return verso_resuelto
	

