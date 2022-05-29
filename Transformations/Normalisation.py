from estimateur.ecarttype import EcartType
from table.Table import Table
from transformations.Transformations import Transformations

class Normalisation(Transformations):
    '''
    Classe de normalisation des tables
    
    '''
    def __init__():
        '''
        Constructeur
        '''
        pass

    def transfo(tab:Table, variable):
        '''
        Normalisation de la variable
        
        Description longue
        ------------------
        Divise les valeurs d'une variable par l'écart-type si celui-ci n'est pas nul
        
        Attributes
        ----------
        tab: Table
            Table sur laquelle on travaille
        variable : str
            nom de la variable qu'on souhaite normaliser
        Examples
        --------
        >>> a1=([Temperature],[[2],[2],[2]])
        >>> a1.normalisation(Temperature)
        ([Temperature],[[1],[1],[1]])
        '''
        donnees=tab.extraire_var(variable)
        ecart = EcartType(donnees).calcul()
        assert(ecart!=0)

        for i in range (len(donnees)):
            donnees[i]=donnees[i]/ecart
        tab.enlev_var(variable)
        tab.ajouter_var(variable,donnees)
        return tab