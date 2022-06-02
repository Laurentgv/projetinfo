from estimateur.moyenne import Moyenne
from table.Table import Table
from transformations.transformation import Transformations

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
        tab: Table
            Table sur laquelle on travaille
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
        donnees=tab.extraire_var(variable)
        moy = Moyenne(donnees).calcul()
        for i in range (len(donnees)):
            donnees[i]=donnees[i]-moy
        tab.enlev_var(variable)
        tab.ajouter_var(variable,donnees)
        return tab