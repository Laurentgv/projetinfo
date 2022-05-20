from Estimateur.moyenne import Moyenne
import Table

class Centrage(Table):
    '''
    '''
    def __init__(self):
        '''
        Constructeur

        '''
        super().__init__()

    def centrage(self,variable):
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
        index=(self.var).index(variable)
        donnees=self.extraire_var(variable)
        moy = Moyenne.calcul(donnees)
        for i in range (len(cop)):
            donnees[i]=donnees[i] - moy
        (self.data)[index]=donnees
        return Table(self.var, self.data)