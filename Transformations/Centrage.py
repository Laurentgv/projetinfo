from estimateur.moyenne import Moyenne
from table.Table import Table
from transformations.Transformations import Transformations

class Centrage(Transformations):
    '''
    '''
    def __init__():
        '''
        Constructeur

        '''
        pass

    def transfo(tab:Table,variable):
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
        print(donnees)
        moy = Moyenne(donnees).calcul(None)
        for i in range (len(donnees)):
            if donnees[i]==None:
                donnees[i]=donnees[i] - moy
        tab.data[index]=donnees
        return Table(tab.var, tab.data)