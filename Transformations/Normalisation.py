from Estimateur.ecarttype import EcartType

class normalisation:
    '''
    '''
    def __init__(self, variable):
        '''
        '''
        self.variable=variable

    def norma(self):
        '''
        Normalisation de la variable
        
        Description longue
        ------------------
        Divise les valeurs d'une variable par l'écart-type si celui-ci n'est pas nul
        
        Attributes
        ----------
        variable : list

        Examples
        --------
        >>> a1=[2,2,2]
        >>> a1.normalisation()
        [1,1,1]
        '''
        ecart = EcartType.calcul(self.variable)
        assert(ecart!=0)
        cop=self.variable
        for i in range (len(cop)):
            cop[i]=cop[i]/ecart
        return cop
    
