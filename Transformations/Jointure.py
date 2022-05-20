from Table import Table

class Jointure():
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

    def __init__(self,tab, var):
        '''
        Constructeur
        
        Attributes
        ----------
        tab : Table
            Table initiale
        var : str
            Variable de la tab1
        '''
        self.tab=tab
        self.var=var

    def transfo(self, tab2, var2):
        '''
        Joint deux tables avec une variable en commun

        Attributes
        ----------
        tab2 : Table
            Table à joindre
        var2 : str
            Variable de tab2 en commun avec var1
        
        Examples
        --------
        '''
        
        tab1=self.tab #table
        var_tab1=tab1.var #list
        var_tab2=tab2.var #list
        i1=tab1.ind(self.var) 
        i2=tab2.ind(var2)
        data1=tab1.data
        data2=tab2.data
        #on vérifie si les colonnes des 2 variables sont égales, sinon pas de jointure possible
        assert(tab1[i1]==tab2[i2])

        #mis à jour de la liste de variables
        for i in range(len(var_tab2)):
            if var_tab2[i]!=var2:
                var_tab1.append(var_tab2[i])
                for j in range(len(tab2)-1):
                    data1[i].append(data2[i][j])
                    
        return Table(var_tab1,data1)
  
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

    def __init__():
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
        variables=[]
        data=[]
        index=self.ind("var")
        
        variables=(self.var)@


        return Table(variables,data)