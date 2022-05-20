from Table import Table
from Estimateur.moyenne import Moyenne

class Moyenne_glissante(Table):
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
    def __init__(self):
        '''
        Constructeur

        '''
        super().__init__()

    def calcul(self,periode):
        '''
        Transformation de la liste en moyenne glissante
        
        Attributes
        ----------
        period : int
            Pas de la moyenne glissante

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
        for i in range (le-periode+1):
            l=[]
            for j in range (periode):
                l.append(data[i+j])
            m=Moyenne.calcul(l)
            L.append(m)
        return L