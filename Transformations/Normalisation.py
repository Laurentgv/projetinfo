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

        Attributes
        ----------
        variable : list

        Examples
        --------
        '''
        ecart = EcartType.calcul(self.variable)
        assert(ecart!=0)

        for i in range (len(self.variable)):
            self.variable[i]=self.variable[i]/ecart

    
