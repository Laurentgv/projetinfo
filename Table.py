from distutils.log import error


class Table:
    '''
    Classe dataframe
    
    Attributes
    ----------
    var = list str
        Liste des noms des variables de la tables
    data = list list
        Tableau des donnees
    '''

    def __init__(self, var, data):
        '''
        Constructeur
        
        Attributes
        ----------
        var : list str
            Liste des noms des variables de la tables
        data : list list
            Tableau des donnees        
        '''
        self.var=var
        self.data=data

    def ind(self, var):
        '''
        Retourne la position d'une variable dans la table
        
        Attributes
        ----------
        var : str
            variable dont on souhaite connaitre l'indice    
        '''
        S=0
        for i in range (len(self.var)):
            if self.var[i]!=var:
                S+=1
        if S==len(self.var):
            return error
        else:
            return S
