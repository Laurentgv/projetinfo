from Estimateur.moyenne import Moyenne
from Table import Table
from Transformations import Transformations

class Centrage(Transformations):
    '''
    '''
    def __init__(self):
        '''
        Constructeur

        '''
        pass

    def transfo(self,tab:Table,variable):
        '''
        Centrage de la variable
        
        Description longue
        ------------------
        Enlève à chaque valeur d'une variable la moyenne de celle-ci

        Attributes
        ----------
        variable : str
            variable dont on souhaite centré les données

        Returns
        -------

        Examples
        --------
        >>> a1=Table([Temperature],[1,2,3])
        >>> a1.centrage(Temperature)
        ([Temperature],[-1,0,1])
        '''
        index=(tab.var).index(variable)
        donnees=tab.extraire_var(variable)
        moy = Moyenne.calcul(donnees)
        for i in range (len(cop)):
            donnees[i]=donnees[i] - moy
        (tab.data)[index]=donnees
        return Table(tab.var, tab.data)