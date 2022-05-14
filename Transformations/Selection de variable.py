class selection_variable:
    '''
    '''
    def __init__(self, tableau):
        '''
        '''
        self.tableau=tableau

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
        for i in range (len(self.tableau)):
            L1.append((i,self.tableau[i][1]))
        print(L1)
        print("Choisissez les variables ques vous souhaitez visualiser.")
        print("Saisissez N si vous avez fini votre saisie")


        a = int(input())
        L2=[]
        while a!="N":
            L2.append(self.tableau[a])
            a = input()
        return L2