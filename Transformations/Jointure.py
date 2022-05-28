from table import Table
from transformations.Transformations import Transformations

class Jointure(Transformations):
    '''
    Classe des jointures de deux tables

    On joint deux tables avec une variable en commun. Il faut égalité entre ces 2 colonnes pour pouvoir joindre les tables

    Attributes
    ----------
    tab : Table
        Table initiale
    var : str
        Variable de la tab1
    '''

    def __init__(self):
        '''
        Constructeur
        '''
        pass

    def transfo(self,tab1:Table, tab2:Table, var):
        '''
        Joint deux tables avec une variable en commun

        Attributes
        ----------
        tab2 : Table
            Table à joindre
        var : str
            Variable de tab2 en commun avec une variable de la table initiale
        
        Examples
        --------
        '''
        variables=(tab1.var)+(tab2.var)
        data=[]
        index=(tab1.var).index("var")
        l=tab1.extraire_var("var")

        for i in range(len(tab1.data)):
            initial=tab1.data[i]
            drap=initial[index]
            i=l.index(drap)
            data.append(initial+tab2[i])
        
        tab=Table(variables,data)
        tab.enlev_var("var") #on enlève la variable var de la table car elle est en double

        return tab