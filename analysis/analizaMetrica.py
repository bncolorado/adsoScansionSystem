#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
23 de mayo de 2015, 31 de julio de 2017.
Recorre un directorio donde habrá uno o más ficheros, con un poema en cada uno.
Genera la estructura XML-TEI para cada poema y lanza el sistema de escansión.
El sistema de escansión determina el patrón métrico de cada verso.
Guarda el fichero resultante en carpeta de salida con el mismo nombre y extensión .xml
'''

import os
from xml.etree import ElementTree as ET
from utilidades import txt2xml_module
from modules import escansion

#Directorios de entrada y salidas
dir_in = 'data_in/Gongora'
dir_out = 'data_out/Gongora'
ruta_diccionario = 'resources/diccionarioFrecuencias.csv'

#Variables generales
log_control = '' #Almacena todos los análisis para revisar errores.
diccionario_de_frecuencias = {} #Para almacenar las frecuencias de aparición de cada patrón métrico.

#Abre fichero de frecuencias y almacena en diccionario.
def abreDiccionario(ruta_diccionario):
	'''Carga un fichero con las frecuencias de cada patrón y lo alamcena como diccionario.'''
	diccionario_salida = {}
	fileDir = os.path.dirname(os.path.realpath('__file__'))
	filename = os.path.join(fileDir, ruta_diccionario)
	diccionario_bruto = open(filename,'rt').read().split('\n') 
	diccionario_bruto = diccionario_bruto[1:-1] #Eliminamos línea 1 (encabezado) y línea final (en blanco)
	for line in diccionario_bruto:
		patron = line.split('\t')[0]
		frecuencia = int(line.split('\t')[1])
		diccionario_salida[patron] = frecuencia
	return diccionario_salida

diccionario_de_frecuencias = abreDiccionario(ruta_diccionario)
for base, directorios, ficheros in os.walk(dir_in): #Recorre directorio y abre fichero uno a uno
	for fichero in ficheros:
		ficheroEntrada = base + '/' + fichero
		directorio = base.split('/')[-1]
		
		if os.path.exists(dir_out+directorio+'/'+fichero) == True: #Comprueba si el fichero ya está analizado:
			print ("El fichero "+fichero+' ya existe.')
		else: 
			print ("Analizando poema "+fichero)
			xml = txt2xml_module.text2xml(ficheroEntrada) #Genera XML-TEI, lo procesa y extrae cada verso (sin etiquetas).
			v = xml.findall('text/body/lg/l')#Extrae cada verso
			versos = [] #Los versos limpios (solo texto, sin etiquetas)
			for item in v:
				versos.append(item.text)
			if versos != []:
				print('XML generado correctamente. Versos del poema extraídos.')
			else:
				print('Ha surgido un problema con el fichero y no se ha podido analizar.')

		#Lanza módulo escansión. La entrada es una lista de versos.
		patrones = escansion.extraePatron(versos, diccionario_de_frecuencias)


		v = xml.findall('text/body/lg/l')#Extraemos cada verso
		for item in v:
			verso = item.text
			item.attrib['met'] = patrones[verso]

		nomFichSalida = fichero[:-4]+'.xml'
		xml_out = txt2xml_module.prettify(xml)
		f =  open(dir_out+'/'+nomFichSalida, 'w')
		f.write(xml_out)
		f.close()

