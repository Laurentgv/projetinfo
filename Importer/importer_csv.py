from importer import Importer
import gzip
import csv
import json
#Permet de faire la liste des fichiers à importer
from os import listdir
from os.path import isfile, join

class Importer_csv(Importer):
    '''Commentaires'''

    def __init__(self) -> None:
        super().__init__()
    
    def csv_do(folderpath:str):
        #Dossier où se trouve le fichier, pour Louis  : 'Downloads/données/données_météo/'
        data_meteo = []
        files = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]
        for filename in files :
            #print(filename)
            with gzip.open(folderpath + filename, mode='rt') as gzfile :
                synopreader = csv.reader(gzfile, delimiter=';') 
                for row in synopreader :
                    data_meteo.append(row)
        #return(len(data_meteo), len(data_meteo[0]))
        return(data_meteo)
    
    def json_do(folderpath:str):
        #Dossier où se trouve le fichier, pour Louis  : 'Downloads/données/données_électricité/'
        data_electricite = []
        files = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]
        for filename in files :
            print(filename)
            with gzip.open(folderpath + filename, mode='rt',encoding='utf-8') as gzfile :
                data_electricite.append(json.load(gzfile))
        return(data_electricite)