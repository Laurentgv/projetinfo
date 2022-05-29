from table import Table
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

    def transfo(self):
        '''
        Transformation de la liste en moyenne glissante
        
        Attributes
        ----------
        Examples
        --------
        >>> import Table
        >>> a=Table(["Nom_variable"],[[24],[3],[3],[3],[3],[3],[3],[3],[9]])
        >>> a.calcul(3)
        [10,3,3,3,3,3,5]
        '''
        L=[]
        var=self.variable
        assert(len(var)==1)
        data=self.data
        le=len(var)
        for i in range (le-self.periode+1):
            l=[]
            for j in range (self.periode):
                l.append(data[i+j])
            m=Moyenne.calcul(l)
            L.append(m)