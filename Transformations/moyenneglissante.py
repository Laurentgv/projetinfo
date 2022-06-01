from table.Table import Table
from estimateur.moyenne import Moyenne
from transformations.Transformations import Transformations

class Moyenne_glissante(Transformations):
    '''
    Classe des transformations par moyenne glissante
    La moyenne glissante modifie une table contenant une seule variable,
    et renvoie une table contenant dans chaque case la moyenne des "periodes"
    valeurs suivantes. On appelle "periode" le pas de la moyenne glissante.
    Attributes
    ----------
    periode : int
        Pas de la moyenne glissante
    '''
    def __init__(self,periode):
        '''
        Constructeur
        Attributes
        ----------
        periode : int
            Pas de la moyenne glissante
        '''
        self.periode=periode

    def transfo(self, table:Table, variable):
        '''
        Transformation de la liste en moyenne glissante
        
        Attributes
        ----------
        table : Table
            Table sur laquelle on travaille
        variable : str
            Variable sur laquelle on veut obtenir une moyenne glissante
        Examples
        --------
        >>> a=Table(['Nom_variable'],[[24],[3],[3],[3],[3],[3],[3],[3],[9]])
        >>> b=Moyenne_glissante(3)
        >>> b.transfo(a, 'Nom_variable')
        Table(['Nom_variable'],[[None],[10],[3],[3],[3],[3],[3],[5],[None]])
        '''
        
        assert(len(var)==1)
        data=table.extraire_var(variable)
        le=len(data)
        L=le*[None]
        start=int(le/self.periode) #on prend la partie entiere, les valeurs avant le start sont des None
        for i in range (start,le-self.periode+1):
            l=[]
            for j in range (self.periode):
                l.append(data[i+j])
            m=Moyenne(l).calcul(None)
            L[i]=m
        table.enlev_var(variable)
        table.ajouter_var(variable,L)
        return table