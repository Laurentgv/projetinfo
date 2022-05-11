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

        Examples
        --------
        '''
        moy = Moyenne.calcul(self.variable)

        for i in range (len(self.variable)):
            self.variable[i]=self.variable[i] - moy
            