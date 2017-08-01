#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marzo 2016 - Junio 2017
@author: jsober, Borja Navarro Colorado

Dado un poema sin ningún tipo de marcado, genera un fichero XML con los versos marcados y un encabezado TEI estándar.

El fichero de entrada debe contener sólo el poema, sin título ni autor ni ningún otro tipo de información. Cada línea debe ser un verso.

"""

import xml.etree.cElementTree as ET
import re
from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem, encoding="UTF-8")
        reparsed = minidom.parseString(rough_string)
        xml = reparsed.toprettyxml(indent = "  ")
        return xml

def createHeader():
        TEIfile = ET.Element("TEI", xmlns = "http://www.tei-c.org/ns/1.0")
        teiHeader = ET.SubElement(TEIfile, "teiHeader")
        fileDesc = ET.SubElement(teiHeader, "fileDesc")
        titleStmt = ET.SubElement(fileDesc, "titleStmt")
        ET.SubElement(titleStmt, "title").text = "Sistema de Escansión Proyecto ADSO: análisis distante del soneto castellano del Siglo de Oro"
        ET.SubElement(titleStmt, "principal").text = "Borja Navarro Colorado"
        ET.SubElement(titleStmt, "funder").text = "Ayuda BBVA a equipos de investigación científica 2016. Proyecto ADSO: análisis distante del soneto castellano del Siglo de Oro."
        respStmt = ET.SubElement(titleStmt, "respStmt")
        ET.SubElement(respStmt, "name")
        ET.SubElement(respStmt, "resp")
        publicationStmt = ET.SubElement(fileDesc, "publicationStmt")
        ET.SubElement(publicationStmt, "publisher").text = "Universidad de Alicante"
        sourceDesc = ET.SubElement(fileDesc, "sourceDesc")
        bibl = ET.SubElement(sourceDesc, "bibl")
        ET.SubElement(bibl, "title").text = "..."
        ET.SubElement(bibl, "author").text = "..."
        ET.SubElement(bibl, "publisher").text = "..."
        ET.SubElement(bibl, "editor").text = "..."
        encodingDesc = ET.SubElement(teiHeader, "encodingDesc")
        metDecl = ET.SubElement(encodingDesc, "metDecl", type = "met", pattern = "(\+|\-)+")
        metDecl.set('xml:id','bncolorado')
        ET.SubElement(metDecl, "metSym",value = "+").text = "sílaba tónica"
        ET.SubElement(metDecl, "metSym",value = "-").text = "sílaba átona"
        metDecl = ET.SubElement(encodingDesc, "metDecl")
        ET.SubElement(metDecl, "p").text = "Todos los patrones métricos han sido extraídos automáticamente con el sistema de escansión del proyecto ADSO"
     
        return TEIfile

def createText(teiFile, soneto, firstLine):
        text = ET.SubElement(teiFile, "text")
        body = ET.SubElement(text, "body")
        head = ET.SubElement(body, "head")
        lg = ET.SubElement(body, "lg")
        ET.SubElement(head, "title").text = firstLine
  		    
        for i in range(len(soneto)):
            numberLine = str(i + 1)    
            ET.SubElement(lg, "l", n = numberLine ,met = "").text = soneto[i]   
      
        return teiFile                
        
###########
#PRINCIPAL#
###########

def text2xml(data_in):
	'''
	La entrada debe ser la ruta a un fichero de texto sencillo con un único soneto (o poema en endecasílabos). El fichero sólo debe contener el texto del poema, sin ningún tipo de marca. Un verso por línea.
	La salida es el poema con las etiquetas XML-TEI (encabezado estándar y versos), y la etiquets de métrica (@met) vacía.
	'''
	soneto = []
	teiFileHeader = createHeader()
	file = open(data_in, 'rt')
	for line in file:
		if (len(line) > 1):
			line = re.sub('\t+', '', line) #Limpia el texto de caracteres innecesarios.
			line = re.sub('\n', '', line)
			line = re.sub('[0-9]', '', line)
			line = re.sub(' $', '', line)
			soneto.append(line)
	firstLine = soneto[0]

	teiFile = createText(teiFileHeader, soneto, firstLine)

	
	return teiFile
