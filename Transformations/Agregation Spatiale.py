from Table import Table
from Transformations import Transformations

class Agregation_spatiale(Transformations):

    '''
    '''
    def __init__(self,variable,L1,L2,L3,L4):
        '''
        Constructeur

        Attributes
        ----------
        variable : str
            variable sur laquelle on fait l'agrégation
        L1 : list
            liste des variables sur laquelle on calcule la moyenne
        L2 : list
            liste des variables sur laquelle on somme les valeurs
        L3 : list 
            liste des variables qu'on retire de la table
        L4 : list
            liste des variables qui ne changent pas sur une agrégation
        
        Examples
        --------
        '''
        self.variable=variable
        self.L1=L1
        self.L2=L2
        self.L3=L3
        self.L4=L4


    def transfo(self,table:Table):
        '''

        Description longue
        ------------------
        

        Attributes
        ----------
    

        Examples
        --------
        '''
        #L3 variables qu'on retire de la table
        for i in range (len(self.L3)):
            table.enlev_var(self.L3[i])

        agreg=list(set(table.extraire_var(self.variable)))
        #Pour séléctionner les valeurs distinctes de la variables
        
        for i in range (len(agreg)):
            compt=(self.variable).count(agreg[i])#nombre d'individu pour chaque agregation
            for a in self.L1:
                #moyenne
                ind=(table.var).index(a) #index de la variable
                m=0
                for j in range (compt):
                    m+=table.data#[l'individu][a]
                m/compt
            for b in self.L2:
                #somme
                ind=(table.var).index(b)
                for j in range (compt):
            for c in self.L4:
                #ne change pas
                ind=(table.var).index(c)