import Table

class Selection_variable(Table):
    '''
    '''
    def __init__(Table):
        '''
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
        >>> a=[[Température, 19, 20, 32],[Ville, Paris, Rennes, Marseille],[Date, 19/04/14, 18/04/14, 24/04/14]]
        >>> a.fun()
        [(1, Température),
        (2, Ville),
        (3, Date)]
        Choisissez les variables ques vous souhaitez visualiser.
        Saisissez N si vous avez fini votre saisie
        >>> 1
        >>> 2
        [[Température, 19, 20, 32],[Ville, Paris, Rennes, Marseille]]
        ''' 
        L1=[]
        for i in range (len(self.var)):
            L1.append((i,self.var[i]))
        print(L1)
        print("Choisissez les variables ques vous souhaitez visualiser.")
        print("Saisissez N si vous avez fini votre saisie")
        a = int(input())
        L2=[]
        while a!="N":
            var=self.var[a]
            donnees=self.data[a]
            L2.append([var]@donnees)
            a = input()
        return L2