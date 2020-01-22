#!/usr/bin/python
# -*- coding: utf-8 -*-

#Dado un verso, realiza un análisis categorial con Freeling.
#Salida: cadena del verso con formato palabra#categoria#lema.

#Basado en:
#https://github.com/TALP-UPC/FreeLing/blob/master/APIs/python/sample.py

#28 de octubre de 2015 - 20 de julio de 2017
#Borja Navarro Colorado & Javier Sober
#Universidad de Alicante

#Dependencia: Freeling 3.0.

import os
import freeling
from subprocess import PIPE, Popen, STDOUT

FREELINGDIR = os.environ.get("FREELINGDIR", "/tools/freeling4");
DATA = FREELINGDIR+"/share/freeling/";
LANG="es";

def analizaFreeling(texto):
    'Dado el nombre de un fichero de texto, lo analiza con Freeling y devuelve el texo analizado'
    # create language analyzer
    #la=freeling.lang_ident(DATA+"common/lang_ident/ident.dat");
    freeling.util_init_locale("default");
    # create options set for maco analyzer. Default values are Ok, except for data files.
    op= freeling.maco_options("es");
    op.set_data_files( "",
                       DATA + "common/punct.dat",
                       DATA + LANG + "/dicc.src",
                       DATA + LANG + "/afixos.dat",
                       "",
                       DATA + LANG + "/locucions.dat",
                       DATA + LANG + "/np.dat",
                       DATA + LANG + "/quantities.dat",
                       DATA + LANG + "/probabilitats.dat");

    # create analyzers
    tk=freeling.tokenizer(DATA+LANG+"/tokenizer.dat");
    sp=freeling.splitter(DATA+LANG+"/splitter.dat");
    mf=freeling.maco(op);

    # activate morpho modules to be used in next call
    if "FREELING_OPTIONS" in os.environ:
        options = list(map(
            lambda x: bool(int(x)),
            os.environ.get("FREELING_OPTIONS", "001010010001")
        ))
        mf.set_active_options(*options)
    else:
        mf.set_active_options(False, False, True, False,  # select which among created
                                True, False, False, True,  # submodules are to be used.
                                False, False, False, True ); # default: all created submodules are used

    # create tagger, sense anotator, and parsers
    tg=freeling.hmm_tagger(DATA+LANG+"/tagger.dat",True,2);
        #sen=freeling.senses(DATA+LANG+"/senses.dat");
        #parser= freeling.chart_parser(DATA+LANG+"/chunker/grammar-chunk.dat");
        #dep=freeling.dep_txala(DATA+LANG+"/dep_txala/dependences.dat", parser.get_start_symbol());

    # process input text
    l = tk.tokenize(texto);
    ls = sp.split(l);

    ls = mf.analyze(ls);
    ls = tg.analyze(ls);

    verso_analizado = CreaFormatoSalida(ls)
    return verso_analizado

def CreaFormatoSalida(outputAnalyzer):
    verso_PoSLema = ''
    for item in outputAnalyzer:
        ws = item.get_words();
        for w in ws:
            if w.get_form() not in ",':;.!?¿¡()«»-`": #Se eliminan signos de puntuación.
                palabra = w.get_form()
                lema = w.get_lemma()
                categoria = w.get_tag()
                verso_PoSLema+=palabra+'#'+categoria+'#'+lema+' '
        verso_PoSLema = verso_PoSLema[:-1]
    return verso_PoSLema

def Analiza(verso=''):
  'Dada un verso, analiza con Freeling la categoría gramatical de cada verso. El verso debe entrar como cadena de texto.'
  verso_analizado = analizaFreeling(verso)
  return verso_analizado
