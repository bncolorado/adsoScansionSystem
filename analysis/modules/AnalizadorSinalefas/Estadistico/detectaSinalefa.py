#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Dado un verso, marca aquellas separaciones silábicas donde se podría dar sinalefa.
#No diferencia entre sinalefa o sinéresis. Se tratan todas igual.

#Borja Navarro Colorado
#2016 - 2017

import string
import re

import modules.AnalizadorSinalefas.PorReglas.resuelvesinalefa
from modules.AnalizadorSinalefas.Estadistico import resolucionporcombinacion

def marcaSinalefas(verso):
	'Detecta aquellas separaciones silábicas donde podría realizarse sinalefa y las marca con el símbolo "#". Almacena el número de POSIBLES sinalefas en "PR".'
	verso = re.sub(' ','-',verso) #Se marcan todos los separados silábicos igual, sin diferenciar entre separación silábica o entre palabras.
	if verso[0] == '-': #Comprobamos que no hay espacio en blanco al inicio del verso.
		verso =  verso[1:]

	PR = 0 #Número de sinalefas que PUEDEN SER resueltas en el verso.

	v = verso.split('-') #Lista con las sílabas del verso.
	c = 0
	salida = ''
	while c < len(v):
		silaba = v[c]
		if c != len(v)-1:
			silaba_posterior = v[c+1]
			if silaba[-1] in u'aeiouyAEIOUYáéíóúÁÉÍÓÚhH' and silaba_posterior[0] in u'haeiouHAEIOUáéíóúÁÉÍÓÚ':
				salida += silaba+'#'
				PR+=1
				c+=1
			elif silaba[-1] in u'aeiouAEIOUáéúíóÁÉÍÓÚyY' and silaba_posterior in 'yYoOuU':
				salida += silaba+'#'
				PR+=1
				c+=1
			else:
				salida += silaba
				c+=1
		else:
			salida += silaba
			c+=1

		salida += '-'

	if salida[-1] == '-': #Comprobamos que no hay guión a final de verso para luego montar bien el verso cojo.
		salida =  salida[:-1]
	return salida, PR

def resuelveVersoNoAmbiguo(verso):
	'Si el verso no es ambiguo (PR=DR), se resuelven todas las posibilidades.'
	verso = re.sub('#-', '', verso)
	return verso

def detectaSinalefas(verso, SinalefasDebeResolver):
	'Marca las sinalefas que se pueden resolver. Deteca si hay ambigüedad: si se pueden resolver más que las que DEBE resolver. Extrae todos los patrones posibles.'
	c = verso.split(' ') 
	c2 = []
	[c2.append(item) for item in c if item not in u' ,:;.!?¿¡()«»-']
	e2 = ' '.join(c2) #Verso con espacio como separación.

	ultSilaba = re.findall('-[a-zA-Z]*$', e2) #Extrae la última sílaba para no tenerla en cuenta en las sinalefas
	ultimaSilaba = ''.join(ultSilaba)

	e2 = re.sub('-[a-zA-Z]*$', '', e2) #Elimina la última sílaba del verso

	verso_marcado, SinalefasPuedeResolver = marcaSinalefas(e2)

	#Control ambigüedad.
	DR = SinalefasDebeResolver #Cantidad de sinalefas que se DEBEN resolver para llegar a 11.
	PR = SinalefasPuedeResolver #Cantidad total de sinalefas que se PUEDEN resolver.

	if DR == PR: #Si coinciden ambos valores, el verso no es ambiguo. Se resuelve.
		verso_resuelto_cojo = resuelveVersoNoAmbiguo(verso_marcado)
		verso_resuelto = verso_resuelto_cojo+ultimaSilaba #Volvemos a colocar al última sílaba en su sitio
		return verso_resuelto

	elif DR < 0 or PR < 0 or DR > PR: #Si hay más necesarias que posibles, se ha producido un error. Se resuevlve por reglas y se toma nota del error.
		print ('\t¡Error! Hay más sinalefas por resolver (DR) que posibilidades de resolución (PR). Se resuelve por reglas.')
		print ('\tDR =', DR, '- PR =', PR)
		#No hace falta poner última síalaba. Lo hace PorReglas.resuelvesinalefa.sinalefa().
		verso_resuelto = modules.AnalizadorSinalefas.PorReglas.resuelvesinalefa.sinalefa(verso, SinalefasDebeResolver) 


		print ('\tEl verso con las sinalefas y/o diéresis resueltas por reglas (a partir de aquí ya no es ambiguo):')
		print('\t', verso_resuelto)
		return verso_resuelto
	
	elif DR < PR: #Si hay más posibles que necesarias, el verso es ambigüo. Se resuelven todas las posibles combinaciones.
		versos_resueltos = ''
		combinaciones_cojo = resolucionporcombinacion.resuelveAmbiguas(verso_marcado, DR, PR)
		for v in combinaciones_cojo:
			versos_resueltos += v+ultimaSilaba+'\n'
		versos_resueltos = versos_resueltos[:-1]
		return versos_resueltos

