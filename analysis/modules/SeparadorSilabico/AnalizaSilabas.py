#!/usr/bin/python
# -*- coding: UTF-8 -*-

#29 de octubre de 2015 - 21 de julio de 2017
#Dado un verso, lo separa en sílabas y marca la sílaba tónica en aquellas palabras que pueden ser métricamente tónicas.
#Borja Navarro Colorado, Javier Sober.


#Recursos:
#1. categoriasTonicas.txt: lista de categorías gramaticales (etiquetas PoS EAGLES) que pueden ser tónicas en un verso.
#2. palabrasAtonas.txt: lista de palabras que son átonas siempre, pero que no se puede especificar por su categoría gramatical.
#3. excepciones_silabeo.txt: palabras que, por cuestiones de prefijación normalmente, no siguen las reglas generales de separación silábica.

import re
from modules.SeparadorSilabico import Acentuacion

def CargaCategoriasTonicas():
	'Carga las categorías gramaticales que pueden ser tónicas (Quilis 1984. Ver guía de anotación). Estas son las reglas para clasificar las palabras de un verso en tónicas o átonas. Para funcionar necesita un fichero .txt con dichas categorías en formato EAGLES-Freling.'
	c = open('./resources/categoriasTonicas.txt', 'rU').read()
	c = re.sub('#.*\n','',c) #Elimina los comentarios del fichero
	categorias = c.split()
	return categorias


def CargaPalabrasAtonas():
	'Palabras átonas son exepciones: palabras que por categoría gramatical deberían ser tónicas, pero que realmente son átonas. Las palabras están en el fichero de texto "palabrasAtonas.txt".'
	p = open('./resources/palabrasAtonas.txt', 'rU').read()
	p = re.sub('#.*\n','',p) #Elimina los comentarios del fichero
	#palabrasAtonas = p.split()
	palabrasAtonas = []
	[palabrasAtonas.append(palabra.lower()) for palabra in p.split()] #Se pasan a minúscual (lower()) para luego comparar en minúscula cno la palabra del verso.
	return palabrasAtonas

def cargaExcepciones():
	'#Carga lista de palabras que, por su configuración morfológica, no siguen las reglas de silabeo generales. En general se refiere a prefijos y sufijos. La lista ha sido creada a partir del trabajo de Antonio Ríos Mestre http://elies.rediris.es/elies4/Fon8.htm'
	e = open('./resources/excepciones_silabeo.txt', 'rU').read()
	e = re.sub('#.*\n','',e) #Elimina los comentarios del fichero
	excep = []
	[excep.append(item) for item in e.split('\n') if item != '']

	excepciones = {}
	for item in excep:
		palabra = item.split(':')[0]
		silabas = item.split(':')[1]
		excepciones[palabra] = silabas
	return excepciones

def separaDieresisGrafica(verso):
	'Separa aquellos diptongos con diéresis gráfica tipo "ruïdo".'
	indice = 0
	salida = ''
	for item in verso:
		if item in 'äëïöüÄËÏÖÜ' and verso[indice-1] not in 'gGqQ':
			if verso[indice+1] in 'hH' and verso[indice+2] in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
				salida += verso[indice]+'-'
			elif verso[indice+1] in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
				salida += verso[indice]+'-'
			else:
				salida += verso[indice]
		elif item in 'äëïöüÄËÏÖÜ' and verso[indice-1] in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
			salida += '-'+verso[indice]
		else:
			salida += verso[indice]
		indice += 1
	return salida

def acentuaAdverbio(palabra, categoria, palabrasAtonas):
	'Separa en sílabas acentúa adverbios (llama a silabeo). Si es adverbio acabado en -mente le asigna doble acentuación.'
	p = Acentuacion.silabeo(palabra) #Separa en sílabas y acentúa el adverbio
	if palabra in palabrasAtonas: #Si está en lista de excepciones, queda átona.
		adverbio=palabra #Si el ADV es "tan", queda átono siempre.
	elif p[-7:] == '-MEN-te' and categoria == 'RG':
		mente = p[-7:]
		adjetivo = p[:-7]
		adjetivo = re.sub('-', '', adjetivo)
		adjetivo_acentuado = Acentuacion.silabeo(adjetivo)
		adverbio = adjetivo_acentuado+mente
	else:
		adverbio=p
	return adverbio

###########
#PRINCIPAL#
###########

def analizaSilabas(verso_analizado):
	'''Dado un verso analizado con PoS (formato Freeling EAGLES), separa las palabras en sílabas, dejando la sílaba tónica en mayúscula y las átonas en minúscula.
	La entrada es una cadena de texto con el formato palabra#categoria#lema.
	La salida es igual que la entrada, salvo que la palabra estará separada en sílabas, quedando las sílabas átonas en minúscula y las tónicas en mayúscula:
	pa-LA-bra#categoría#lema'''

	excepciones = cargaExcepciones()
	categorias = CargaCategoriasTonicas()
	palabrasAtonas = CargaPalabrasAtonas()

	#Limpieza del verso:
	verso_analizado = re.sub('a#SP#a el#DA0MS0#el', 'al#SP#al', verso_analizado) #Se unen las contracciones separadas por FreeLing
	verso_analizado = re.sub('de#SP#de el#DA0MS0#el', 'del#SP#del', verso_analizado)

	silabas = ''
	for item in verso_analizado.split(' '):
		palabra_raw = item.split('#')[0]
		palabra_dieresisSeparada = separaDieresisGrafica(palabra_raw) #Separamos ya la diéresis
		palabra = palabra_dieresisSeparada.lower() #Se pasa a minúscula para no confudir luego con las mayúsculas que indican sílaba tónica.
		categoria_raw = item.split('#')[1]
		categoria = categoria_raw[:2] #Sólo usamos la información categorial más general: posiciones 1 y 2 de la etiqueta EAGLES.
		lema = item.split('#')[2]

		if palabra in excepciones.keys(): #si la palabra está en diccionario de excepciones, la salida es la forma ya analizada que está en el diccionario. No accede por silabeo.py.
			silabas += excepciones[palabra]+' '

		elif categoria in 'RG': #Caso de adverbio se analizan aparte por la doble acentuación de "-mente".
			adverbio = acentuaAdverbio(palabra, categoria, palabrasAtonas)
			silabas += adverbio+' '


		elif item == verso_analizado.split(' ')[-1]: #Si es la última palabra, se acentúa (sea cual sea su categoría gramatical). Se llama a silabeo.py Esta opción no es muy robusta. Pensar otra...
			ultima_palabra = Acentuacion.silabeo(palabra)
			silabas += ultima_palabra+' '

		elif categoria in categorias: #Caso con categoría tónica:
			if palabra in palabrasAtonas: #Si está en lista de excepciones, queda átona.
				silabas +=  palabra+' '
			else: #Si no está en la lista de excepciones, queda tal y como la devuelve el silabificador.
				palabra_en_silabas = Acentuacion.silabeo(palabra) 
				silabas +=  palabra_en_silabas+' '

		else: #Resto de casos se consideran categorías átonas (minúscula).
			palabra_en_silabas = Acentuacion.silabeo(palabra) 
			silabas += palabra_en_silabas.lower()+' '

	silabas = silabas[:-1] #En la cadena queda un espacio en blanco al final que es aquí eliminado.
	return silabas


