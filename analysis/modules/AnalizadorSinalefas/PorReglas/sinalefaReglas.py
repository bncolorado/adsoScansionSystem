#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 8 de octubre de 2013
#Establece las reglas de sinalefa como funciones. Solo las reglas.

#Borja Navarro Colorado
#Universida de Alicante

import string
import re

#Dos sílabas átonas

def uneatonas(verso, sinlalefPorResolver):
        indice = int()
        salida = ''
        for item in verso:
            if item == ' ' and indice < (len(verso)-1):
                if verso[indice-1] in 'aeiouh,;.:' and verso[indice+1] in 'aeiouh':
                    if sinlalefPorResolver > 0:
                        salida += u'_'
                        sinlalefPorResolver = sinlalefPorResolver-1
                    else:
                        salida += item
                else:
                    salida += item
            else:
                salida += item
            indice += 1
        return salida, sinlalefPorResolver

def sineresisAtonas(verso, sinlalefPorResolver):
        indice = int()
        salida = ''
        for item in verso:
            if item == u'-' and indice < (len(verso)-1):
                if verso[indice-1] in 'haeiou,;.:' and verso[indice+1] in 'aeiouh':
                    if sinlalefPorResolver > 0:
                        salida += u'_'
                        sinlalefPorResolver = sinlalefPorResolver-1
#					print sinlalefPorResolver
                    else:
                        salida += item
                else:
                    salida += item
            else:
                salida += item
            indice += 1
        return salida, sinlalefPorResolver

def enmedioConjuncionAtonaDcha(verso, sinlalefPorResolver): #Une la conjunción con la palabra de la derecha
        indice = int()
        salida = ''
        for item in verso:
            if item == u' ':
                if verso[indice-1] in u'yaeouh' and (verso[indice-2] == ' ' or verso[indice-2] == '_') and verso[indice+1] in u'aeiouh':
                    if sinlalefPorResolver > 0:
                        salida += u'_'
                        sinlalefPorResolver = sinlalefPorResolver-1
                    else:
                        salida += item
                else:
                    salida += item
            else:
                salida += item
            indice += 1
        return salida, sinlalefPorResolver

def enmedioConjuncionAtonaIzq(verso, sinlalefPorResolver): #Une la conjunción con la palabra de la izquierda
        indice = int()
        salida = ''
        for item in verso:
            if item == ' ':
                if verso[indice-1] in u'aeiouh' and verso[indice+1] in u'yaeouh' and verso[indice+2] == ' ':
                    if sinlalefPorResolver > 0:
                        salida += u'_'
                        sinlalefPorResolver = sinlalefPorResolver-1
                    else:
                        salida += item
                else:
                    salida += item
            else:
                salida += item
            indice += 1
        return salida, sinlalefPorResolver


#Una sílaba átona y otra tónica

def SineresisTonicaAtona(verso, sinlalefPorResolver):
    indice = int()
    salida = ''
    for item in verso:
        if item == u'-':
            if verso[indice-1] in u'HAEIOUÁÉÍÓÚ' and verso[indice+1] in u'aeiouh':
                if sinlalefPorResolver > 0:
                    salida += u'_'
                    sinlalefPorResolver = sinlalefPorResolver-1
                else:
                    salida += item
            else:
                salida += item
        else:
            salida += item
        indice += 1
    return salida, sinlalefPorResolver

def sineresisAtonaTonica(verso, sinlalefPorResolver):
    indice = int()
    salida = ''
    for item in verso:
        if item == u'-':
            if verso[indice-1] in u'aeiouh' and verso[indice+1] in u'AEIOUÁÉÍÓÚH':
                if sinlalefPorResolver > 0:
                    salida += u'_'
                    sinlalefPorResolver = sinlalefPorResolver-1
                else:
                    salida += item
            else:
                salida += item
        else:
            salida += item
        indice += 1
    return salida, sinlalefPorResolver


def uneaTonicaAtona(verso, sinlalefPorResolver):
    indice = int()
    salida = ''
    for item in verso:
        if item == ' ':
            if verso[indice-1] in u'AEIOUÁÉÍÓÚH' and verso[indice+1] in u'aeiouh':
                if sinlalefPorResolver > 0:
                    salida += u'_'
                    sinlalefPorResolver = sinlalefPorResolver-1
                else:
                    salida += item
            else:
                salida += item
        else:
            salida += item
        indice += 1
    return salida, sinlalefPorResolver

def uneaAtonaTonica(verso, sinlalefPorResolver):
    indice = int()
    salida = ''
    for item in verso:
        if item == ' ':
            if verso[indice-1] in u'aeiouh' and verso[indice+1] in u'AEIOUÁÉÍÓÚH':
                if sinlalefPorResolver > 0:
                    salida += u'_'
                    sinlalefPorResolver = sinlalefPorResolver-1
                else:
                    salida += item
            else:
                salida += item
        else:
            salida += item
        indice += 1
    return salida, sinlalefPorResolver

def enmedioConjuncionTonicaDcha(verso, sinlalefPorResolver):
    indice = int()
    salida = ''
    for item in verso:
        if item == ' ':
            if verso[indice-1] in u'yaeouh' and verso[indice-2] == ' ' and verso[indice+1] in u'AEIOUÁÉÍÓÚH': #Une conjunción con vocal izquierda
                if sinlalefPorResolver > 0:
                    salida += u'_'
                    sinlalefPorResolver = sinlalefPorResolver-1
                else:
                    salida += item
            else:
                salida += item
        else:
            salida += item
        indice += 1
    return salida, sinlalefPorResolver

def enmedioConjuncionTonicaIzq(verso, sinlalefPorResolver):
    indice = int()
    salida = ''
    for item in verso:
        if item == ' ':
            if verso[indice-1] in u'AEIOUÁÉÍÓÚHY' and verso[indice+1] in u'yaeouh' and verso[indice+2] == ' ':#Une conjución con vocal derecha
                if sinlalefPorResolver > 0:
                    salida += u'_'
                    sinlalefPorResolver = sinlalefPorResolver-1
                else:
                    salida += item
            else:
                salida += item
        else:
            salida += item
        indice += 1
    return salida, sinlalefPorResolver



#Dos sílabas tónicas

def incioConjuncionAtona(verso, sinlalefPorResolver):
    indice = int()
    salida = ''
    for item in verso:
        if item == ' ':
            if verso[indice-1] in u'yaeiou' and indice-1 == 0 and verso[indice+1] in u'aeiouAEIOUÁÉÍÓÚhH':
                if sinlalefPorResolver > 0:
                    salida += u'_'
                    sinlalefPorResolver = sinlalefPorResolver-1
                else:
                    salida += item
            else:
                salida += item
        else:
            salida += item
        indice += 1
    return salida, sinlalefPorResolver


def incioConjuncionTonica(verso, sinlalefPorResolver):
    indice = int()
    salida = ''
    for item in verso:
        if item == ' ':
            if verso[indice-1] in u'YAEIOUÁÉÍÓÚ' and indice-1 == 0 and verso[indice+1] in u'aeiouAEIOUÁÉÍÓÚhH':
                if sinlalefPorResolver > 0:
                    salida += u'_'
                    sinlalefPorResolver = sinlalefPorResolver-1
                else:
                    salida += item
            else:
                salida += item
        else:
            salida += item
        indice += 1
    return salida, sinlalefPorResolver

def uneaTonicas(verso, sinlalefPorResolver):
    indice = int()
    salida = ''
    for item in verso:
        if item == ' ':
            if verso[indice-1] in u'AEIOUÁÉÍÓÚH' and verso[indice+1] in u'AEIOUÁÉÍÓÚH':
                if sinlalefPorResolver > 0:
                    salida +=u'_'
                    sinlalefPorResolver = sinlalefPorResolver-1
                else:
                    salida += item
            else:
                salida += item
        else:
            salida += item
        indice += 1
    return salida, sinlalefPorResolver

