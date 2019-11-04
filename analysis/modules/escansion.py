## -*- coding: utf-8 -*-
##escansion.py : Sistema de Escansión Métrica. Módulo principal.
##Octubre 2015 - julio 2017
##Borja Navarro Colorado
##Universidad de Alicante

##Llama por orden al resto de módulos y gestiona entradas y salidas
##La salida es un diccionario {verso:patrón}, donde "patrón" tien el formato requerido para incorporarlo al XML-TEI.

import re
import subprocess

from modules.AnalizadorCategorial import AnalizaCategoriaGramaticalFreeling
from modules.SeparadorSilabico import AnalizaSilabas
from modules.Contador import cuentasilabas
from modules.ExtraePatron import extraepatron
from modules.AnalizadorSinalefas.Estadistico import detectaSinalefa
from modules.AnalizadorSinalefas.Estadistico import detectaDieresis
from modules.AnalizadorSinalefas.Estadistico import desambiguadorPorFrecuencias

salida = {} #Diccionario donde cada verso (item) tiene su patrón final asociaco (patron)

def modernizaTexto(item):
	'''Modernización del texto: normalización de apóstrofos y otros elementos.'''
	#Casos específicos:
	item = re.sub("ni'n", "ni en", item)
	item = re.sub("d'él", "de él", item)
	item = re.sub("qu'l", "que el", item)
	item = re.sub("qu'en", "que en", item)
	#Caso general
	item = re.sub("([a-zA-Z])'h*([a-záéíóúA-ZÁÉÍÓÚ])", lambda match: "{}{} {}".format(match.group(1), match.group(2), match.group(2)), item)
	item = re.sub("([a-záéíóúA-ZÁÉÍÓÚ])'h*([a-zA-Z])", lambda match: "{} {}{}".format(match.group(1), match.group(1), match.group(2)), item)
	#Fórmulas de tratamiento.
	item = re.sub(" V. M. ", " vuestra merced ", item)
	#item = re.sub("(,|;|\.|:|!|\?|¡|¿)",  "", item) #Eliminamos signos de puntuación.
	#item = re.sub(" ?(B|C|D|F|G|H|J|K|L|M|N|P|Q|R|S|T|W|Y|Z) ",  " ", item) #Eliminamos consonantes sueltas, que dan error de silabifiación.
	return item

def extraePatron(versos, diccionario_de_frecuencias):
    'Asigna un patrón métrico a cada verso. La entrada es una lista donde cada elemento es un verso. La salida es un diccionario {verso:patron}'
    salida = {}
    n=1 #Número de verso analizado

    for item in versos: #itera sobre cada verso y lanza las funciones
        number = str(n)
        print ('\nAnalizando verso '+ number +': "'+ item  +'"')

	#0. Moderniza y arregla el texto.
        item = modernizaTexto(item)
        print('\t1. Texto modernizado: '+item)

	#1. Análisis categorial.
        verso_analizado = AnalizaCategoriaGramaticalFreeling.Analiza(verso=item)
        print('\t2. Análisis categorial realizado:')
        print(u'\t'+verso_analizado)


	#2. Separador silábico: análisis de sílaba tónica y clasificación de palabras en tónica o átona.
        print('\t3. Separación silábica y acentuación')
        verso_en_silabas = AnalizaSilabas.analizaSilabas(verso_analizado)
        print('\t'+verso_en_silabas)

	#3. Contador.
        contador = cuentasilabas.cuentasilabas(verso_en_silabas)
        print('\tNúmero de sílabas antes de procesar sinalefas o diéresis:', contador)

	#4. Calcula número de sinalefas por resolver (estadístico) y genera patrón para todos los casos.
        if contador == 11:
               patron = extraepatron.extraepatron(verso_en_silabas)
               print('\t4. Verso no ambiguo:', patron)

        elif contador < 11: #Casos de diéresis
            dieresis_por_resolver = 11-contador
            verso_final = detectaDieresis.detectaDieresis(verso_en_silabas, dieresis_por_resolver) #Resuelve diéresis
            if '\n' not in verso_final:
                patron = extraepatron.extraepatron(verso_final)
                print('\t4. Verso con dieresis no ambiguo:')
                print('\t'+verso_final, patron)
            else:
               versos = verso_final.split('\n')
               patrones = ''
               p_ambiguo = ''
               for v in versos:
                   print('\t'+v)
                   p = extraepatron.extraepatron(v)
                   print('\t'+p)
                   if p not in patrones: #Evita repetir patrones iguales de un mismo verso
                       patrones+=p+'\n'
                   if p not in p_ambiguo: #Evita repetir patrones iguales de un mismo verso
                       p_ambiguo+=p+'\t'
               if patrones[-1] == '\n':
	               patrones = patrones[:-1]
               patron = desambiguadorPorFrecuencias.desambiguaPorFrecuencia(patrones, diccionario_de_frecuencias)
               print('\t4. Verso ambiguo con diéresis desambiguado:', patron)
        else:
            sinalefas_por_resolver = contador-11 #Cantidad de sinalefas que se deben resolver para llegar a 11.
            verso_final = detectaSinalefa.detectaSinalefas(verso_en_silabas, sinalefas_por_resolver)
            #Genera patrón. Comprueba si hay uno o varios:
            if '\n' not in verso_final:
               patron = extraepatron.extraepatron(verso_final)
               print('\t4. Verso con sinalefa no ambiguo:', patron)
            else:
              print("\tVerso ambiguo por sinalefa")
              versos = verso_final.split('\n')
              patrones = ''
              p_ambiguo = ''
              for v in versos:
                  p = extraepatron.extraepatron(v)
                  if p not in patrones: #Evita repetir patrones iguales de un mismo verso
                      patrones+=p+'\n'
                  if p not in p_ambiguo: #Evita repetir patrones iguales de un mismo verso
                      p_ambiguo+=p+'\t'
                  #p=p[:-1]
              if patrones[-1] == '\n':
	              patrones = patrones[:-1]
              patron = desambiguadorPorFrecuencias.desambiguaPorFrecuencia(patrones, diccionario_de_frecuencias)
              print('\t4. Patrón final:', patron)
        n+=1
        salida[item] = patron
    return salida

