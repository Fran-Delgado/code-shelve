# code_shelve_crear.py

import shelve
import os

path_base =os.getcwd()
dir_trabajo = "code_shelve"
fichero = "mis_datos"

os.chdir(os.path.join(path_base,dir_trabajo))

fichero = shelve.open(fichero)

pigs = ['Zophie_pig', 'Pooka_pig', 'Simon_pig']
cats = ['Zophie_cat', 'Pooka_cat', 'Simon_cat']

fichero['pigs'] = pigs
fichero['cats'] = cats

fichero.close()