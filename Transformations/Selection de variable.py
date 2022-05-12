class selection_variable:
    '''
    '''
    def __init__(self, tableau):
        '''
        '''
        self.tableau=tableau

    def fun(self):
        '''
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