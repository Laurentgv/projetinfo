from table.Table import Table
from transformations.Transformations import Transformations

class Jointure(Transformations):
    '''
    Classe des jointures de deux tables

    On joint deux tables avec une variable en commun. Il faut égalité entre ces 2 colonnes pour pouvoir joindre les tables

    Attributes
    ----------
    '''

    def __init__(self):
        '''
        Constructeur
        '''
        pass

    def transfo(tab1:Table, tab2:Table, var):
        '''
        Joint deux tables avec une variable en commun

        Attributes
        ----------
        tab1 : Table
            Table initiale
        tab2 : Table
            Table à joindre
        var : str
            Variable de tab2 en commun avec une variable de la table initiale
        
        Examples
        --------
        '''
        variables=(tab1.var)+(tab2.var)
        data=[]
        index=(tab1.var).index(var) #numéro de la variable dans la table 1
        l2=tab2.extraire_var(var) #liste de données de la variable dans tab 2

        for i in range(len(tab1.data)):
            initial=tab1.data[i]
            drap=initial[index]
            if not(drap in l2):
                data.append(None)
            else:
                i=l2.index(drap) #numéro de l'individu possédent la variable commune
                data.append(initial+tab2[i])
        
        tab=Table(variables,data)
        tab.enlev_var(var) #on enlève la variable car de la table car elle est en double

        return tab