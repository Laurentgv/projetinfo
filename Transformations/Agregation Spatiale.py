class agregation_spatiale:
    '''
    '''
    def __init__(self, tableau, variable):
        '''
        '''
        self.variable=variable
        self.tableau=tableau

    def selection(self):
        '''
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
            return self.tableau
        else: #peut probablement être optimisé
            nom=L2[a]
            for j in range (len(self.variable)): 
                if self.variable[j]==nom:
                    L3.append(self.tableau[j])
            return L3
