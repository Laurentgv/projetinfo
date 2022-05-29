from table.Table import Table
from transformations.Transformations import Transformations

class Selection_variable(Transformations):
    '''
    '''
    def __init__(self, variable):
        '''
        Constructeur

        Attributes
        ----------
        variable : list str
            liste des variables qui constituent la nouvelle table
        '''
        self.variable=variable

    def transfo(self,tab:Table):
        '''
        Permet à l'utilisateur de choisir les variables qu'il souhaite visualiser.

        Description longue
        ------------------
        L'utilisateur doit saisir les variables qu'il souhaite visualiser.
        Une nouvelle table est ensuite créée avec les variables que l'utilisateur a choisi.

        Attributes
        ----------

        Examples
        --------
        >>> a=Table([Température, Ville, Date],[[19,Paris,140418],[20,Rennes,140418],[32,Marseille,140424]])
        >>> a.fun()
        [(1, Température),
        (2, Ville),
        (3, Date)]
        Table([Température, Ville],[[19,Paris],[20,Rennes],[32,Marseille]])
        ''' 

        l=self.variable
        table=Table(l,[])
        for i in range (len(l)):
            don=tab.extraire_var(l[i])
            table.ajouter_var(l[i],don)
        return table