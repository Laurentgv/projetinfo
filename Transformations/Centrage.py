from Estimateur.moyenne import Moyenne

class centrage:
    '''
    '''
    def __init__(self, variable):
        '''
        '''
        self.variable=variable

    def centrage(self):
        '''
        Centrage de la variable

        Attributes
        ----------
        variable : list

        Returns
        -------
        list

        Examples
        --------
        >>> a1=[1,2,3]
        >>> a1.centrage()
        [0.5,1,1.5]
        '''
        moy = Moyenne.calcul(self.variable)
        cop = self.variable
        for i in range (len(cop)):
            cop[i]=cop[i] - moy
        return cop