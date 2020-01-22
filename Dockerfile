FROM herchu/freeling4-es:pub
# Built from https://github.com/bncolorado/adsoScansionSystem/
# To use it:
# $ docker run -it -v $(pwd):/adso/data_in -v $(pwd):/adso/data_out linhdpostdata/adso
# Where data_in contains plain text files to be analyzed and data_out will contain the output after the analysis is done.
ENV DATA_IN="data_in"
ENV DATA_OUT="data_out"

# See https://freeling-user-manual.readthedocs.io/en/latest/modules/maco/
# Current options are as specified by Borja-Navarro
# for the ADSO 100 Poem Corpus:
# "Freeling debe estar configurado para que NO analice expresiones temporales.
#  [...] Es la opción "--nodate" de $analyze.
#  En principio debe tener desactivas las opciones de "multiword expressions"
#  (--noloc), "number detection" (--nonumb), "affix analysis" (--noafx),
#  "Named Entities" (--noner) y magnitudes ("--noquant"). El sistema de
#  escansión espera etiquetas categoriales, por lo que estas opciones de
#  Freeling deben estar desactivadas."
# This translates to 001010010001 in Freeling maco options
# Original options were 011111011111
ENV FREELINGDIR="/usr"
ENV FREELING_OPTIONS="001010010001"

RUN apt-get update
RUN apt-get install python3-lxml -y

COPY ./analysis /adso
WORKDIR /adso/

RUN cp /home/APIs/python/*freeling* .

CMD ["python3", "analizaMetrica.py"]
