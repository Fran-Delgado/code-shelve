import shelve
import os

path_base =os.getcwd()
dir_trabajo = "code_shelve"
fichero = "mis_datos"

os.chdir(os.path.join(path_base,dir_trabajo))

fichero = shelve.open(fichero)
print(fichero['cats'])
print(fichero['pigs'])
fichero.close()
