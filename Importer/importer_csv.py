from numpy import character
from importer import Importer
import gzip
import csv

class Importer_csv(Importer):
    '''Commentaires'''

    def __init__(self) -> None:
        super().__init__()

    
    def do(self, folderpath):
    # Dossier où se trouve le fichier  : '/Users/Louis/Downloads/données/données_météo/'
        data = []
        for i in folderpath : 
            filename = str(i)
            with gzip.open(folderpath + filename, mode='rt') as gzfile :
                synopreader = csv.reader(gzfile, delimiter=';') 
                for row in synopreader :
                    data.append(row)
        return(data)
