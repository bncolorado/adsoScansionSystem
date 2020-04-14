# -*- coding: utf-8 -*-
import random

#Dado un verso con varios patrones métrico posibles, selecciona el más frecuente.
#Depende del diccionario de frecuencias calculado en la fase de entrenamiento (ver directorio "Recursos").

#13 de noviembre de 2015
#Borja Navarro Colorado
#Universidad de Alicante

#Consulta diccionario y extrae la frecuencia de cada patron de entrada
#Recuerda que el diccionario de frecuencias se ha cargado al inicio del proceso, en el script principal.

def desambiguaPorFrecuencia(patrones_cadena, diccionario_frecuencias):
	'''Dada una serie de patrones, da como salia el más frecuente según un diccionario de frecuencias'''
	dic = diccionario_frecuencias
	patron_fq = []
	patrones = patrones_cadena.split('\n')
	if len(patrones) == 1: #Se comprueba si sólo hay uno ya que, al no repetir patrones, puede ser que todas las opciones de sinalefa den un único patrón. En este caso, se devuelve lo que entra y sigue.
		patronMasFrecuente = patrones_cadena
	else:
		for item in patrones:
			if item in dic:
				patron_fq.append((dic[item], item))
		patron_fq.sort()
		patronMasFrecuente = patron_fq[-1][1] if patron_fq else random.choice(patrones) #Salida solo el verso ambiguo.
	return patronMasFrecuente

