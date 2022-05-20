from Estimateur.moyenne import Moyenne

class Centrage:
    '''
    '''
    def __init__(self, variable):
        '''
        '''
        self.variable=variable

    def centrage(self):
        '''
        Centrage de la variable
        
        Description longue
        ------------------
        Enlève à chaque valeur d'une variable la moyenne de celle-ci

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
        [-1,0,1]
        '''
        moy = Moyenne.calcul(self.variable)
        cop = self.variable
        for i in range (len(cop)):
            cop[i]=cop[i] - moy
        return cop