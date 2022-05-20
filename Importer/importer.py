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
        '''Permet d'importer un fichier json.
        
        Paramètres
        ----------
        filepath : str
            Chemin complet du fichier que l'on veut importer
            
        Retourne
        --------
        data : list of dict
            Une liste de dictionnaire
            data[x] permet d'accéder à l'individu x
            Dans le cadre du projet chaque individu est un dictionnaire de 4 items : datasetid, recordid, fields et record_timestamp.
            Les données se trouvent essentiellement dans fields qui est lui même un dictionnaire à 5 items.
            
        Exemples
        --------
        >>>2013_01 = json_do(Downloads/données/données_électricité/2013-01.json.gz)
        >>>2013_01[0]
        >>>{'datasetid': 'consommation-quotidienne-brute-regionale', 'recordid': 'e28e41fe8a890eed00e49c0849255351c5413c50', 'fields': {'code_insee_region': '24', 'date': '2013-01-01', 'region': 'Centre-Val de Loire', 'date_heure': '2013-01-01T00:00:00+01:00', 'heure': '00:00'}, 'record_timestamp': '2018-04-26T08:49:58.532+02:00'}
        >>>2013_01[0]['datasetid']
        >>>'consommation-quotidienne-brute-regionale'
        >>>2013_01[0]['fields']['region']
        >>>'Centre-Val de Loire'
        '''
        data=[]
        with gzip.open(filepath, mode='rt',encoding='utf-8') as gzfile :
            data=json.load(gzfile)

        return data


doc = "/Users/laurentgv/Desktop/PTD - données/synop.201301.csv.gz"
t = Importer.csv_file(doc)
print (t[0])