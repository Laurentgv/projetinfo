from Estimateur.ecarttype import EcartType
import Table

class Normalisation(Table):
    '''
    '''
    def __init__(self):
        '''
        Constructeur

        '''
        super().__init__()

    def norma(self, variable):
        '''
        Normalisation de la variable
        
        Description longue
        ------------------
        Divise les valeurs d'une variable par l'écart-type si celui-ci n'est pas nul
        
        Attributes
        ----------
        variable : str
            nom de la variable qu'on souhaite normaliser

        Examples
        --------
        >>> a1=([Temperature],[[2],[2],[2]])
        >>> a1.normalisation(Temperature)
        ([Temperature],[[1],[1],[1]])
        '''
        index=(self.var).index(variable)
        ecart = EcartType.calcul((self.var)[index])
        assert(ecart!=0)
        donnees=self.extraire_var(variable)
        for i in range (len(cop)):
            donnees[i]=donnees[i]/ecart
        (self.data)[index]=donnees
        return Table(self.var,self.data)
    
