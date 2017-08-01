# A metrical scansion system for fixed-metre Spanish poetry (analysis)

Version 3.1.1 - July 2017
Borja Navarro Colorado
University of Alicante

Here is the code of the paper "A metrical scansion system for fixed-metre Spanish poetry" *Digital Scholarship in the Humanities*, 2017,  doi: https://doi.org/10.1093/llc/fqx009.

## Introduction - What's this?

An authomatic scansion system of Spanish poetry. The system takes a verse as input and return its meter. Stressed syllables are represented with the symbol "+" and unstressed syllables with the symbol "-". For example:

​	` En tanto que de rosa y azucena: -----+---+-`

The system combines hand-made rules and frequency information. It has been trained with the [Corpus of Spanish Golden-Age Sonnets (with metrical annotation)](https://github.com/bncolorado/CorpusSonetosSigloDeOro). The code to train the system with your own corpus will be available soon.

For the moment it runs only for Spanish sonnets —it is ready to analyse hendesayllables (eleven syllables). A new version for polyrithmic poetry is nowadays underdevelopment. Stay tuned!

## Instalation

The system is a set of python scripts. To run the system you must install  Python 3.x (https://www.python.org/)

Moreover, the system depends on [Freeling](http://nlp.lsi.upc.edu/freeling/) to analyze the Part of Speech of each word. It must be installed and running in you computer. How to install Freeling, please see http://nlp.lsi.upc.edu/freeling/node/8 

To run the system, unzip it on a directory and run analizaMetrica.py

`python3.x analizaMetrica.py`

where x is the version of your python.

It has been tested in Linux and MacOS. If you find any problem, please, contact me.

## Running the system

To analyze you own poems, follow these steps:

1. Put all your sonnets (see input format below) in the "data_in" folder and create a "data_out" folder in the same directory
2. (Alternatively, you can create "data_in" and "data_out" folders in any place in your computer and edit the route to these folders in "dir_in" and "dir_out" in analizaMetrica.py)
3. Run `python3.x analizaMetrica.py`
4. At the end, all poems analyzed will be stored in "data_out" folder.
5. During the process, the system will be printing on the screen the steps carried out. If you want to store this information in a file, run  `python3.x analizaMetrica.py > log.txt` 

## Input and output format

As input, all poems must be plain text. A poem per file with .txt extension.

Output fomat is  a XML-TEI fiel (.xml extension) with a standard TEI-Header and a tag `@met`to represent the metre. TEI-Header can be edited in "utilidades/txt2xml.py". For detaills about the output format, please see:

Borja Navarro Colorado, María Ribes Lafoz and Noelia Sánchez (2016) 
"Metrical annotation of a large corpus of Spanish sonnets: 
representation, scansion and evaluation", Proceedings of the [10th edition of the Language Resources and Evaluation Conference](http://lrec2016.lrec-conf.org/en/), 23-28 May 2016, Portorož (Slovenia) [[PDF](http://www.dlsi.ua.es/%7Eborja/453_Paper.pdf)].

## How to cite the system

If you use this tool for academic research purposes, please cite it whit the following reference:

Navarro-Colorado, Borja (2017) "A metrical scansion system for fixed-metre Spanish poetry" *Digital Scholarship in the Humanities*,  doi: https://doi.org/10.1093/llc/fqx009

https://academic.oup.com/dsh/article-abstract/doi/10.1093/llc/fqx009/3064339/A-metrical-scansion-system-for-fixed-metre-Spanish