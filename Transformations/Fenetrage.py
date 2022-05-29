from datetime import datetime
import time
from table.Table import Table
from transformations.Transformations import Transformations

class Fenetrage(Transformations):
    '''
    Sélection des données sur une période temporelle
    '''
    def __init__(self):
        '''
        Constructeur

        '''
        pass

    def transfo(tab:Table):
        '''

        Permet à l'utilisateur d'obtenir les individus entre 2 dates qu'il aura à saisir

        Description longue
        ------------------
        L'utilisateur devra saisir date et heure de début et de sortie.
        Il obtiendra ensuite seulement les individus dont la data se trouve entre les dates qu'il aura saisi.

        Attributes
        ----------
        tab : Table
            Table des variables et données

        Examples
        --------
        '''
        print("Saisir date de début au format AnnéeMoisJour")
        date_debut=input()
        print("Saisir date de fin au format AnnéeMoisJour")
        date_fin=input()

        debut=datetime.strptime(str(date_debut), '%Y%m%d')
        fin=datetime.strptime(str(date_fin),'%Y%m%d')

        if debut>fin:
            raise Exception("Attention votre date de fin est antérieure à la date de début")
        indice = tab.var.index("date_heure")
        data=tab.data
        L=[]
        for i in range (len(data)):
            actuel=data[i][indice]
            if (actuel.year>=debut.year) and (actuel.year<=fin.year) and (actuel.month>=debut.month) and (actuel.month<=fin.month) and (actuel.day>=debut.day) and (actuel.day<=fin.day): 
                L.append(data[i])

        return Table((tab.var),L)


