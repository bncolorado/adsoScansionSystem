#!/usr/bin/python
# -*- coding: UTF-8 -*-

#6 de septiembre de 2013 - 8 de octubre de 2013
#Se aplican las reglas de resolución de sinalefas por orden,
#según Quilis, de la menos forzada a la más forzada.
#Finaliza cuando llega a 11 sílabas.

import re
from modules.AnalizadorSinalefas.PorReglas import dieresis02
from modules.AnalizadorSinalefas.PorReglas import sinalefaReglas

def sinalefa(verso, sinlalefPorResolver): 
    c = verso.split(' ') 
    c2 = []
    [c2.append(item) for item in c if item not in u' ,:;.!?¿¡()«»-']

    e2 = ' '.join(c2)

    ultSilaba = re.findall(u'-[a-zA-Z]*$', e2) #Extrae la última sílaba para no tenerla en cuenta en las sinalefas
    ultimaSilaba = ''.join(ultSilaba)

    entrada2 = re.sub(u'-[a-zA-Z]*$', '', e2) #Elimina la última sílaba del verso

    if sinlalefPorResolver < 0:
        salida = dieresis02.dieresis(entrada2, sinlalefPorResolver, ultimaSilaba)
        return salida
    else:
        while sinlalefPorResolver > 0:
            try:
                salida, sinlalefPorResolver = sinalefaReglas.uneatonas(entrada2, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.sineresisAtonas(salida, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.enmedioConjuncionAtonaDcha(salida, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.enmedioConjuncionAtonaIzq(salida, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.SineresisTonicaAtona(salida, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.sineresisAtonaTonica(salida, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.uneaTonicaAtona(salida, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.uneaAtonaTonica(salida, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.enmedioConjuncionTonicaDcha(salida, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.enmedioConjuncionTonicaIzq(salida, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.incioConjuncionAtona(salida, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.incioConjuncionTonica(salida, sinlalefPorResolver)
                salida, sinlalefPorResolver = sinalefaReglas.uneaTonicas(salida, sinlalefPorResolver)
            finally: #sinlalefPorResolver > 0: #Rompemos el bucle, para los casos en que no se puede llegar a 11.
                salida2 = salida+ultimaSilaba
                return salida2
        salida2 = salida+ultimaSilaba
        return salida2

