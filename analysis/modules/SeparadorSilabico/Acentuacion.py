#!/usr/bin/python
# -*- coding: utf-8 -*-

#Copyright (C) 2007  Rafael C. Carrasco
#This program is free software; you can redistribute it and/or
#modify it under the terms of   the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#Adapted from José A. Mañas in Communications of the ACM 30(7), 1987.


# A class that performs simple hypenation of Spanish words.
# It does not work with foreign words as pa-ra-psi-co-lo-gía: 
# hyphenated as in cáp-su-la.

#Implementado en Pytho por Javier Sober

import re
import lxml  

v = "[aáeéiíoóuúü]"            # vowels
a = "[aáeéíoóú]"               # open vowels
i = "[iuü]"                    # closed vowels
c = "[bcdfghjklmnñpqrstvxyz]"  # consonants       
r = "[hlr]"                    # liquid and mute consonants
b = "[bcdfgjkmnñpqstvxyz]"     # non-liquid consonants
P = [];
P.append("(" + i + "h" + i + ")")
P.append("(" + a + "h" + i + ")")
P.append("(" + i + "h" + a + ")")
P.append("(" + "." + c + r + v + ")")
P.append("(" + c + r + v + ")")
P.append("(" + "." + c + v + ")")
P.append("(" + a + a + ")")
P.append("(" + "." + ")")

all =  P[0] + "|"  + P[1] + "|" + P[2] + "|" + P[3] +  "|"+ P[4] + "|" + P[5] + "|"  + P[6] + "|" + P[7]
prog = re.compile(all)

    

# Return separator if matching pattern is 4,6 or 7
def getGroup( x ):
    switcher = {
        4: '-',
        6: '-',
        7: '-',     
    }
    return switcher.get(x, "")

## Hyphenates a word.
## @param The word to be hyphenated.
## @return hyphenation.    
def parse ( input ):
    output = ""
    while (len(input)>0):
        output += input[0]
        ## Return first matching pattern.
        m = prog.search(input)
        output += getGroup(m.lastindex)
        input = input[1:]
     
    return output;

def buscarTilde( silabas ):
    tildes = "[áéíóú]"
    reg = re.compile(tildes)
    pos = 0
    for sil in silabas:
        if (reg.search(sil)):
            return pos
        pos += 1    
    
    return -1
    
def buscarTonica( silabas ):
    tonica = "(([aeiou])|(n)|([aeiou]s))\Z"
    reg = re.compile(tonica)
    if (reg.search(silabas[len(silabas)-1])):
        return True  
    else:
        return False        
    
    
    
def acentuacion ( silabas ):
    if (len(silabas) == 1):
        silabas[0] = silabas[0].upper()
    else:
        tilde = buscarTilde(silabas)
        if (tilde != -1):
            silabas[tilde] = silabas[tilde].upper()
        elif (buscarTonica(silabas)):
            silabas[len(silabas)-2] = silabas[len(silabas)-2].upper()
        else:
            silabas[len(silabas)-1] = silabas[len(silabas)-1].upper()
    
    palabra = "-".join(str(x) for x in silabas)
            
    return palabra

def silabeo(word):
    out = ''
    wordre = []
    wordre = word.split(" ")
    #wordre = re.compile("\w+",re.UNICODE | re.IGNORECASE)
    l = word
    #delete .decode('utf8')

    for m in wordre:
#        sys.stdout.write(u[pos:m.start()].encode('utf8'))
        #delete .encode('utf8')
        #out += (u[pos:m.start()])
        #w = m.group(0)
        l = parse(m).split("-")       
        t = acentuacion(l)
        #d = u"".join(jeperipi(w))
#        sys.stdout.write(d.encode('utf8'))
        #.encode('utf8')
        out += (t)+" "
        #.encode('utf8')
    out = out[:len(out)-1]
    return out
         
