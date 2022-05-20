class Agregation_spatiale:
    '''
    '''
    def __init__(self, data, variable):
        '''
        '''
        self.variable=variable
        self.data=data

    def selection(self):
        '''
        Permet à l'utilisateur de choisir les régions dont il souahite observer les valeurs.

        Description longue
        ------------------
        L'utilisateur doit saisir les régions qu'il souhaite visualiser.
        Une nouvelle table est ensuite créée avec les régions que l'utilisateur a choisi.
        L'utilisateur peut aussi choisir de visualiser les données pour toute la France

        Attributes
        ----------
        variable : list
            variable dont on souhaite observer les valeurs
        
        data : (list of list) or (list of dict)
            table dont on souhaite observer les valeurs

        Examples
        --------
        >>> a=[]
        >>> a.fun()
        [(1, Ille-et-Villaine),
        (2, Ile-de-France),
        (3, Normandie)]
        Quelles régions souhaitez vous visualiser ? Entrez France si vous souhaitez tout visualiser.
        >>> 1
        >>> 2
        
        '''
        L2=[]
        L3=[]
        L1=set(self.variable)
        L1=list(L1)
        #Pour séléctionner les valeurs distinctes de la variables
        for i in range (len(L1)):
            L2.append((i,L1[i]))
        print(L2)
        print("Quelles régions souhaitez vous visualiser ? Entrez France si vous souhaitez tout visualiser.")
        a=int(input())
        if a=="France":
            return self.data
        else: #peut probablement être optimisé
            nom=L2[a]
            for j in range (len(self.variable)): 
                if self.variable[j]==nom:
                    L3.append(self.data[j])
            return L3
