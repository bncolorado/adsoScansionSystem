#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Reglas de separación de diptongos (expresiones regulares).
#Damos cuenta de todos los casos, los posibles y los imposibles, y dejamos que sea el módulo estadístico el que decida la mejor opción (el patrón métrico resultante más común).
#Los grupos vocálicos con diéresis gráfica se han separado ya (obligatorio).

#Borja Navarro Colorado
#Universidad de Alicante
#2015-2017

import re

def separadieresis(silaba):
	salida = ''

	#############Débil+Débil####################################

	##ui##

	if re.search(u'([A-Z]*[^Q|^G])UI', silaba) != None:
		silaba = re.sub(u'([A-Z]*[^Q|^G]?)UI', lambda match: u'{}u-I'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*[^q|^g]?)ui', silaba) != None:
		silaba = re.sub(u'([a-z]*[^q|^g]?)ui', lambda match: u'{}u-i'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'ÚI([A-Z]*)', silaba) != None:
		silaba = re.sub(u'ÚI([A-Z]*)', lambda match: u'Ú-i{}'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UÍ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UÍ', lambda match: u'{}u-Í'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UHI', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UHI', lambda match: u'{}u-HI'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'ÚHI([A-Z]*)', silaba) != None:
		silaba = re.sub(u'ÚHI([A-Z]*)', lambda match: u'Ú-hi{}'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UHÍ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UHÍ', lambda match: u'{}u-HÍ'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*)uhi', silaba) != None:
		silaba = re.sub(u'([a-z]*)uhi', lambda match: u'{}u-hi'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	##iu##
	
	elif re.search(u'([A-Z]*)IU', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IU', lambda match: u'{}i-U'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida
		
	elif re.search(u'([a-z]*)iu', silaba) != None:
		silaba = re.sub(u'([a-z]*)iu', lambda match: u'{}i-u'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'ÍU([A-Z]*)', silaba) != None:
		silaba = re.sub(u'ÍU([A-Z]*)', lambda match: u'Í-u{}'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IÚ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IÚ', lambda match: u'{}i-Ú'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IHU', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IHU', lambda match: u'{}i-HU'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'ÍHU([A-Z]*)', silaba) != None:
		silaba = re.sub(u'ÍHU([A-Z]*)', lambda match: u'Í-hu{}'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IHÚ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IHÚ', lambda match: u'{}i-HÚ'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*)ihu', silaba) != None:
		silaba = re.sub(u'([a-z]*)ihu', lambda match: u'{}i-hu'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida
	
		
	##########Débil+Fuerte###############################################################
	##ua, ue, uo##
	
	elif re.search(u'([A-Z]*)UA', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UA', lambda match: u'{}u-A'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*)ua', silaba) != None:
		silaba = re.sub(u'([a-z]*)ua', lambda match: u'{}u-a'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*[^Q|^G])UE', silaba) != None:
		silaba = re.sub(u'(([A-Z]*[^Q|^G]))UE', lambda match: u'{}u-E'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*[^q|^g])ue', silaba) != None:
		silaba = re.sub(u'([a-z]*[^q|^g])ue', lambda match: u'{}u-e'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UO', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UO', lambda match: u'{}u-O'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*)uo', silaba) != None:
		silaba = re.sub(u'([a-z]*)uo', lambda match: u'{}u-o'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UÁ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UÁ', lambda match: u'{}u-Á'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UÉ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UÉ', lambda match: u'{}u-É'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UÓ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UÓ', lambda match: u'{}u-Ó'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UHA', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UHA', lambda match: u'{}u-HA'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UHE', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UHE', lambda match: u'{}u-HE'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UHO', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UHO', lambda match: u'{}u-HO'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UHÁ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UHÁ', lambda match: u'{}u-HÁ'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UHÉ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UHÉ', lambda match: u'{}u-HÉ'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UHÓ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UHÓ', lambda match: u'{}u-HÓ'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	##ia, ie, io##

	elif re.search(u'([A-Z]*)IA', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IA', lambda match: u'{}i-A'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*)ia', silaba) != None:
		silaba = re.sub(u'([a-z]*)ia', lambda match: u'{}i-a'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IE', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IE', lambda match: u'{}i-E'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)ie', silaba) != None:
		silaba = re.sub(u'([A-Z]*)ie', lambda match: u'{}i-e'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IO', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IO', lambda match: u'{}i-O'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*)io', silaba) != None:
		silaba = re.sub(u'([a-z]*)io', lambda match: u'{}i-o'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IÁ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IÁ', lambda match: u'{}i-Á'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IÉ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IÉ', lambda match: u'{}i-É'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IÓ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IÓ', lambda match: u'{}i-Ó'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IHA', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IHA', lambda match: u'{}i-HA'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IHE', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IHE', lambda match: u'{}i-HE'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IHO', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IHO', lambda match: u'{}i-HO'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IHÁ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IHÁ', lambda match: u'{}i-HÁ'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IHÉ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IHÉ', lambda match: u'{}i-HÉ'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)IHÓ', silaba) != None:
		silaba = re.sub(u'([A-Z]*)IHÓ', lambda match: u'{}i-HÓ'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida


	##########Fuerte+Débil###############################################################
	##au, eu, ou##

	elif re.search(u'([A-Z]*)AU', silaba) != None:
		silaba = re.sub(u'([A-Z]*)AU', lambda match: u'{}a-U'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*)au', silaba) != None:
		silaba = re.sub(u'([a-z]*)au', lambda match: u'{}a-u'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)EU', silaba) != None:
		silaba = re.sub(u'([A-Z]*)EU', lambda match: u'{}e-U'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*)eu', silaba) != None:
		silaba = re.sub(u'([a-z]*)eu', lambda match: u'{}e-u'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)UO', silaba) != None:
		silaba = re.sub(u'([A-Z]*)UO', lambda match: u'{}u-O'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*)uo', silaba) != None:
		silaba = re.sub(u'([a-z]*)uo', lambda match: u'{}u-o'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

#CASOS DUDOSOS:
#	elif re.search(u'([A-Z]*)UÁ', silaba) != None:
#		silaba = re.sub(u'([A-Z]*)UÁ', lambda match: u'{}u-Á'.format(match.group(1).lower()), silaba)
#		salida += silaba
#		return salida

#	elif re.search(u'([A-Z]*)UÉ', silaba) != None:
#		silaba = re.sub(u'([A-Z]*)UÉ', lambda match: u'{}u-É'.format(match.group(1).lower()), silaba)
#		salida += silaba
#		return salida

#	elif re.search(u'([A-Z]*)UÓ', silaba) != None:
#		silaba = re.sub(u'([A-Z]*)UÓ', lambda match: u'{}u-Ó'.format(match.group(1).lower()), silaba)
#		salida += silaba
#		return salida

	elif re.search(u'([A-Z]*)AHU', silaba) != None:
		silaba = re.sub(u'([A-Z]*)AHU', lambda match: u'{}a-HU'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)EHU', silaba) != None:
		silaba = re.sub(u'([A-Z]*)EHU', lambda match: u'{}e-HU'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)OHU', silaba) != None:
		silaba = re.sub(u'([A-Z]*)OHU', lambda match: u'{}o-HU'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	#elif re.search(u'([A-Z]*)UHÁ', silaba) != None:
	#	silaba = re.sub(u'([A-Z]*)UHÁ', lambda match: u'{}u-HÁ'.format(match.group(1).lower()), silaba)
	#	salida += silaba
	#	return salida

	#elif re.search(u'([A-Z]*)UHÉ', silaba) != None:
	#	silaba = re.sub(u'([A-Z]*)UHÉ', lambda match: u'{}u-HÉ'.format(match.group(1).lower()), silaba)
	#	salida += silaba
	#	return salida

	#elif re.search(u'([A-Z]*)UHÓ', silaba) != None:
	#	silaba = re.sub(u'([A-Z]*)UHÓ', lambda match: u'{}u-HÓ'.format(match.group(1).lower()), silaba)
	#	salida += silaba
	#	return salida


	##ai, ei, oi##

	elif re.search(u'([A-Z]*)AI', silaba) != None:
		silaba = re.sub(u'([A-Z]*)AI', lambda match: u'{}a-I'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*)ai', silaba) != None:
		silaba = re.sub(u'([a-z]*)ai', lambda match: u'{}a-i'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)EI', silaba) != None:
		silaba = re.sub(u'([A-Z]*)EI', lambda match: u'{}e-I'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)ei', silaba) != None:
		silaba = re.sub(u'([A-Z]*)ei', lambda match: u'{}e-i'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)OI', silaba) != None:
		silaba = re.sub(u'([A-Z]*)OI', lambda match: u'{}o-I'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([a-z]*)oi', silaba) != None:
		silaba = re.sub(u'([a-z]*)oi', lambda match: u'{}o-i'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	#elif re.search(u'([A-Z]*)IÁ', silaba) != None:
	#	silaba = re.sub(u'([A-Z]*)IÁ', lambda match: u'{}i-Á'.format(match.group(1).lower()), silaba)
	#	salida += silaba
	#	return salida

	#elif re.search(u'([A-Z]*)IÉ', silaba) != None:
	#	silaba = re.sub(u'([A-Z]*)IÉ', lambda match: u'{}i-É'.format(match.group(1).lower()), silaba)
	#	salida += silaba
	#	return salida

	#elif re.search(u'([A-Z]*)IÓ', silaba) != None:
	#	silaba = re.sub(u'([A-Z]*)IÓ', lambda match: u'{}i-Ó'.format(match.group(1).lower()), silaba)
	#	salida += silaba
	#	return salida

	elif re.search(u'([A-Z]*)AHI', silaba) != None:
		silaba = re.sub(u'([A-Z]*)AHI', lambda match: u'{}a-HI'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)EHI', silaba) != None:
		silaba = re.sub(u'([A-Z]*)EHI', lambda match: u'{}e-HI'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	elif re.search(u'([A-Z]*)OHI', silaba) != None:
		silaba = re.sub(u'([A-Z]*)OHI', lambda match: u'{}o-HI'.format(match.group(1).lower()), silaba)
		salida += silaba
		return salida

	#elif re.search(u'([A-Z]*)IHÁ', silaba) != None:
	#	silaba = re.sub(u'([A-Z]*)IHÁ', lambda match: u'{}i-HÁ'.format(match.group(1).lower()), silaba)
	#	salida += silaba
	#	return salida

	#elif re.search(u'([A-Z]*)IHÉ', silaba) != None:
	#	silaba = re.sub(u'([A-Z]*)IHÉ', lambda match: u'{}i-HÉ'.format(match.group(1).lower()), silaba)
	#	salida += silaba
	#	return salida

	#elif re.search(u'([A-Z]*)IHÓ', silaba) != None:
	#	silaba = re.sub(u'([A-Z]*)IHÓ', lambda match: u'{}i-HÓ'.format(match.group(1).lower()), silaba)
	#	salida += silaba
	#	return salida

	#####################################################################################

	else:
		salida += silaba
		return salida
