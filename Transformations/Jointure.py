from Table import Table

class Jointure(Table):
    '''
    Classe des jointures de deux tables

    On joint deux tables avec une variable en commun. Il faut égalité entre ces 2 colonnes pour pouvoir joindre les tables

    Attributes
    ----------
    tab : Table
        Table initiale
    var : str
        Variable de la tab1
    '''

    def __init__(self):
        '''
        Constructeur
        '''
        super().__init__()

    def joint(self,tab2, var):
        '''
        Joint deux tables avec une variable en commun

        Attributes
        ----------
        tab2 : Table
            Table à joindre
        var : str
            Variable de tab2 en commun avec une variable de la table initiale
        
        Examples
        --------
        '''
        variables=(self.var)+(tab2.var)
        data=[]
        index=(self.var).index("var")
        l=(tab2).extraire_var("var")

        for i in range(len(self.data)):
            initial=self.data[i]
            drap=initial[index]
            i=l.index(drap)
            data.append(initial+tab2[i])
        
        tab=Table(variables,data)
        tab.enlev_var("var") #on enlève la variable var de la table car elle est en double

        return tab