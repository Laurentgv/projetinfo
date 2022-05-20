import gzip
import csv
import json


class Importer():
    '''Cette classe permet d'importer des fichiers csv ou json. 
    Peut-être qu'on pourra lui rajouter la possibilté d'importer directement un dossier de fichier(...?)

    Attributs
    ---------
    Faut il mettre le chemin du fichier en attribut de la classe ou en attribut des méthodes, question à poser.

    Méthodes
    --------
    csv_file(filepath:str) : 
        Permet d'importer un fichier csv, en indiquant le chemin complet du fichier.

    json_file(filepath:str) : 
        Permet d'importer un fichier json, en indiquant le chemin complet du fichier.

    Exemples
    --------
    >>>synop_201301 = csv_do('Downloads/données/données_météo/synop.201301.csv.gz')
    >>>2013_01 = json_do(Downloads/données/données_électricité/2013-01.json.gz)
    '''

    def __init__(self) -> None:
        super().__init__()

    def csv_file(filepath:str):
        '''Permet d'importer un fichier csv.

        Paramètres
        ----------
        filepath : str
            C'est le chemin complet du fichier que l'on veut importer

        Retourne
        --------
        data : list of list
            On renvoie une liste de liste des données importées. Les données sont rangées de la manière suivante : data[ligne][colonne]=data[individu][variable].
            Avec data[0][0] qui correspond à la liste des noms des variables.

        Exemples
        --------
        >>>synop_201301 = csv_do('Downloads/données/données_météo/synop.201301.csv.gz')
        >>>synop_201301[0][0]
        >>>['numer_sta', 'date', 'pmer', 'tend', 'cod_tend', 'dd', 'ff', 't', 'td', 'u', 'vv', 'ww', 'w1', 'w2', 'n', 'nbas', 'hbas', 'cl', 'cm', 'ch', 'pres', 'niv_bar', 'geop', 'tend24', 'tn12', 'tn24', 'tx12', 'tx24', 'tminsol', 'sw', 'tw', 'raf10', 'rafper', 'per', 'etat_sol', 'ht_neige', 'ssfrai', 'perssfrai', 'rr1', 'rr3', 'rr6', 'rr12', 'rr24', 'phenspe1', 'phenspe2', 'phenspe3', 'phenspe4', 'nnuage1', 'ctype1', 'hnuage1', 'nnuage2', 'ctype2', 'hnuage2', 'nnuage3', 'ctype3', 'hnuage3', 'nnuage4', 'ctype4', 'hnuage4', '']
        '''
        data = []
        with gzip.open(filepath, mode='rt') as gzfile :
            synopreader = csv.reader(gzfile, delimiter=';') 
            for row in synopreader :
                data.append(row)
        return(data)
    
    def json_file(self, filepath:str):

        data=[]
        with gzip.open(filepath, mode='rt',encoding='utf-8') as gzfile :
            data=json.load(gzfile)

        return data


doc = "/Users/laurentgv/Desktop/PTD - données/synop.201301.csv.gz"
t = Importer.csv_file(doc)
print (t[0])