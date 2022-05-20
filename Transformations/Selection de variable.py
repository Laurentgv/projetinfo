from Table import Table

class Selection_variable(Table):
    '''
    '''
    def __init__(Table):
        '''
        Constructeur
        '''
        super().__init__()

    def fun(self):
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
        Choisissez les variables ques vous souhaitez visualiser.
        Saisissez N si vous avez fini votre saisie
        >>> 1
        >>> 2
        Table([Température, Ville],[[19,Paris],[20,Rennes],[32,Marseille]])
        ''' 

        for i in range (len(self.var)):
            print((i,self.var[i]))
        print("Choisissez les variables ques vous souhaitez visualiser.")
        print("Saisissez N si vous avez fini votre saisie")

        data=self.data
        a = input()
        assert(a!="N")
        L2=[a]
        var=[]
        donnees=[]
        while a!="N":
            var.append(self.var[a])
            a = input()
            L2.append(a)
        for i in range (len(data)):
            l=[]
            for j in range (len(L2)):
                z=L2[j]
                l.append(data[i][z])
            donnees.append(l)
        return Table(var,donnees)