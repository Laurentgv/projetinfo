from tkinter import _EntryIndex
import outils

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

#   def ind(self, var):
#       '''
#       Retourne la position d'une variable dans la table
#       
#       Attributes
#       ----------
#       var : str
#          variable dont on souhaite connaitre l'indice    
#        '''
#        S=0
#        for i in range (len(self.var)):
#            if self.var[i]!=var:
#                S+=1
#        if S==len(self.var):
#            raise Exception("Attention! La variable n'appartient pas à cette table")
#        else:
#            return S

    def enlev_var(self,variable):
        '''
        Permet de retirer une variable à une table
        
        Attributes
        ----------
        var : str
            variable qu'on souhaite retirer
        
        Example
        -------
        >>> a=Table([pays,temperature],[[France,12],[UK,14]])
        >>> a.enlev_var("temperature")
        Table([pays],[[France],[UK]])
        '''

        index=(self.var).index(variable)
        var=self.var
        var.pop(index)
        data=self.data
        for j in range (len(data)):
            (data[j]).pop(index)
        return Table(var,data)

    def ajouter_var(self,variable,donnees):
        '''
        Permet d'ajouter une variable à une table
        
        Attributes
        ----------
        variable : str
            nom de la variable qu'on souhaite ajouter
        donnees : list
            ensemble des valeurs de la variable ajoutée

        Example
        -------
        >>> a=Table([pays],[[France],[UK]])
        >>> a.ajouter_var("temperature", [12,14])
        a=Table([pays,temperature],[[France,12],[UK,14]])
        '''
        variables=self.var
        data=self.data
        variables.append(variable)
        for i in range (len(data)):
            (data[i]).append(donnees[i])
        return (Table(variables,data))

    def extraire_var(self,variable):
        '''
        Permet d'extraire les données d'une variable dans une table
        
        Attributes
        ----------
        variable : str
            Nom de la variable qu'on souhaite
        '''
        index=(self.var).index(variable)
        L=[]
        for i in range(len(self.data)):
            L.append((self.data)[i][index])
        return L
