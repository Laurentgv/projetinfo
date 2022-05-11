from estimateur import Estimateur

class Somme(Estimateur):
    '''Un estimateur, la somme de toutes les observations sur une variable
    '''

    def __init__(self, variable):
        self.variable=variable

    def calcul(self):
        S=0
        for i in range(len(self.variable)):
            S+=self.variable[i]
        return S
