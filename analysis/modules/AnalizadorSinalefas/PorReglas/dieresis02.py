#!/usr/bin/python
# -*- coding: UTF-8 -*-

#4 de octubre de 2013 - 8 de octubre de 2013
#Si el verso tiene menos de 11 sílabas, localiza los casos de dieresis y separa los diptongos.
#Controla el número de sílabas resultante al aplicar cada regla. Si llega a 11, sale.
#Las reglas se aplican por orden.

import re

#casos de diéresis con signo ortográfico (diéres obligada por el autor)
#Esto ya se ha hecho antes. Dejo la función aquí por si hubiera algún error.
def separaDieresis(verso, sinlalefPorResolver, ultimaSilaba):
	indice = int()
	salida = ''
	for item in verso:
		if item in unicode('äëïöüÄËÏÖÜ', 'utf8') and verso[indice-1] not in unicode('gGqQ', 'utf8'):
			if sinlalefPorResolver < 0:
				if verso[indice+1] in 'hH' and verso[indice+2] in 'aeiouAEIOU':
					salida += verso[indice]+'-'
				elif verso[indice+1] in 'aeiouAEIOU':
					salida += verso[indice]+'-'
				else:
					salida += verso[indice]
				sinlalefPorResolver = sinlalefPorResolver+1
		else:
			salida += verso[indice]
		indice += 1
	return salida, sinlalefPorResolver, ultimaSilaba

#Casos ambigüos

def casosAmbiguos(verso, sinlalefPorResolver, ultimaSilaba):
	while sinlalefPorResolver < 0:

	###Débil+Débil###
		if re.search(u'([A-Z]*[^Q|^G])UI', verso) != None:
			verso = re.sub(u'([A-Z]*[^Q|^G]?)UI', lambda match: u'{}u-I'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)IU', verso) != None:
			verso = re.sub(u'([A-Z]*)IU', lambda match: u'{}i-U'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([a-z]*[^q|^g]?)ui', verso) != None:
			verso = re.sub(u'([a-z]*[^q|^g]?)ui', lambda match: u'{}u-i'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([a-z]*)iu', verso) != None:
			verso = re.sub(u'([a-z]*)iu', lambda match: u'{}i-u'.format(match.group(1).lower()), verso)
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba


		if re.search(u'ÍU([A-Z]*)', verso) != None:
			verso = re.sub(u'ÍU([A-Z]*)', lambda match: u'Í-u{}'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'ÚI([A-Z]*)', verso) != None:
			verso = re.sub(u'ÚI([A-Z]*)', lambda match: u'Ú-i{}'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)IÚ', verso) != None:
			verso = re.sub(u'([A-Z]*)IÚ', lambda match: u'{}i-Ú'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)UÍ', verso) != None:
			verso = re.sub(u'([A-Z]*)UÍ', lambda match: u'{}u-Í'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba

		if re.search(u'([A-Z]*)IHU', verso) != None:
			verso = re.sub(u'([A-Z]*)IHU', lambda match: u'{}i-HU'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)UHI', verso) != None:
			verso = re.sub(u'([A-Z]*)UHI', lambda match: u'{}u-HI'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'ÍHU([A-Z]*)', verso) != None:
			verso = re.sub(u'ÍHU([A-Z]*)', lambda match: u'Í-hu{}'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'ÚHI([A-Z]*)', verso) != None:
			verso = re.sub(u'ÚHI([A-Z]*)', lambda match: u'Ú-hi{}'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)IHÚ', verso) != None:
			verso = re.sub(u'([A-Z]*)IHÚ', lambda match: u'{}i-HÚ'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)UHÍ', verso) != None:
			verso = re.sub(u'([A-Z]*)UHÍ', lambda match: u'{}u-HÍ'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([a-z]*)uhi', verso) != None:
			verso = re.sub(u'([a-z]*)uhi', lambda match: u'{}u-hi'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([a-z]*)ihu', verso) != None:
			verso = re.sub(u'([a-z]*)ihu', lambda match: u'{}i-hu'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1

	###Débil+Fuerte###
		if re.search(u'([A-Z]*)UA', verso) != None:
			verso = re.sub(u'([A-Z]*)UA', lambda match: u'{}u-A'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([a-z]*)ua', verso) != None:
			verso = re.sub(u'([a-z]*)ua', lambda match: u'{}u-a'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba

		if re.search(u'([A-Z]*)UE', verso) != None:
			verso = re.sub(u'([A-Z]*)UE', lambda match: u'{}u-E'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba

		if re.search(u'([a-z]*)ue', verso) != None:
			verso = re.sub(u'([a-z]*)ue', lambda match: u'{}u-e'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba


		if re.search(u'([A-Z]*)UO', verso) != None:
			verso = re.sub(u'([A-Z]*)UO', lambda match: u'{}u-O'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba

		if re.search(u'([A-Z]*)UÁ', verso) != None:
			verso = re.sub(u'([A-Z]*)UÁ', lambda match: u'{}u-Á'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)UÉ', verso) != None:
			verso = re.sub(u'([A-Z]*)UÉ', lambda match: u'{}u-É'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)UÓ', verso) != None:
			verso = re.sub(u'([A-Z]*)UÓ', lambda match: u'{}u-Ó'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba

		if re.search(u'([A-Z]*)UHA', verso) != None:
			verso = re.sub(u'([A-Z]*)UHA', lambda match: u'{}u-HA'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)UHE', verso) != None:
			verso = re.sub(u'([A-Z]*)UHE', lambda match: u'{}u-HE'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)UHO', verso) != None:
			verso = re.sub(u'([A-Z]*)UHO', lambda match: u'{}u-HO'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba

		if re.search(u'([A-Z]*)UHÁ', verso) != None:
			verso = re.sub(u'([A-Z]*)UHÁ', lambda match: u'{}u-HÁ'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)UHÉ', verso) != None:
			verso = re.sub(u'([A-Z]*)UHÉ', lambda match: u'{}u-HÉ'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)UHÓ', verso) != None:
			verso = re.sub(u'([A-Z]*)UHÓ', lambda match: u'{}u-HÓ'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba


		if re.search(u'([A-Z]*)IA', verso) != None:
			verso = re.sub(u'([A-Z]*)IA', lambda match: u'{}i-A'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([a-z]*)ia', verso) != None:
			verso = re.sub(u'([a-z]*)ia', lambda match: u'{}i-a'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)IE', verso) != None:
			verso = re.sub(u'([A-Z]*)IE', lambda match: u'{}i-E'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)IO', verso) != None:
			verso = re.sub(u'([A-Z]*)IO', lambda match: u'{}i-O'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba

		if re.search(u'([a-z]*)io', verso) != None:
			verso = re.sub(u'([a-z]*)io', lambda match: u'{}i-o'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba


		if re.search(u'([A-Z]*)IÁ', verso) != None:
			verso = re.sub(u'([A-Z]*)IÁ', lambda match: u'{}i-Á'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)IÉ', verso) != None:
			verso = re.sub(u'([A-Z]*)IÉ', lambda match: u'{}i-É'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)IÓ', verso) != None:
			verso = re.sub(u'([A-Z]*)IÓ', lambda match: u'{}i-Ó'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
	
		if re.search(u'([A-Z]*)IHA', verso) != None:
			verso = re.sub(u'([A-Z]*)IHA', lambda match: u'{}i-HA'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)IHE', verso) != None:
			verso = re.sub(u'([A-Z]*)IHE', lambda match: u'{}i-HE'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)IHO', verso) != None:
			verso = re.sub(u'([A-Z]*)IHO', lambda match: u'{}i-HO'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba

		if re.search(u'([A-Z]*)IHÁ', verso) != None:
			verso = re.sub(u'([A-Z]*)IHÁ', lambda match: u'{}i-HÁ'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)IHÉ', verso) != None:
			verso = re.sub(u'([A-Z]*)IHÉ', lambda match: u'{}i-HÉ'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba
		if re.search(u'([A-Z]*)IHÓ', verso) != None:
			verso = re.sub(u'([A-Z]*)IHÓ', lambda match: u'{}i-HÓ'.format(match.group(1).lower()), verso)
			sinlalefPorResolver+=1
			if sinlalefPorResolver == 0:
				return verso, sinlalefPorResolver, ultimaSilaba

		return verso, sinlalefPorResolver, ultimaSilaba
	
###########
#PRINCIPAL#
###########

def dieresis(v, sinlalefPorResolver, ultimaSilaba):
	verso = unicode(v, 'utf-8') #Pasamos la cadena de entrada a Unicode para dar cuenta de diéresis (signo)
	out, sinlalefPorResolver, ultimaSilaba = separaDieresis(verso, sinlalefPorResolver, ultimaSilaba)
	if sinlalefPorResolver == 0:
		out2 = out+ultimaSilaba
		return out2.encode('UTF8')
	elif sinlalefPorResolver < 0:
		salida, sinlalefPorResolver, ultimaSilaba = casosAmbiguos(out, sinlalefPorResolver, ultimaSilaba)
		out2 = salida+ultimaSilaba
		return out2.encode('UTF8')

