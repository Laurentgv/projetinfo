from importer import Importer

class Importer(Importer):
    import gzip
    import csv
    # Dossier où se trouve le fichier  :
    folder = 'Users/Louis/Desktop/'
    filename = 'synop.201301.csv.gz'
    data = []
    with gzip.open(folder + filename, mode='rt') as gzfile :
        synopreader = csv.reader(gzfile, delimiter=' ;') 
        for row in synopreader :
            data.append(row)
