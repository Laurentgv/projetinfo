from Table import Table
from Transformations import Transformations

class Agregation_spatiale(Transformations):

    '''
    '''
    def __init__(self,variable,L1,L2,L3,L4):
        '''
        Constructeur

        Attributes
        ----------
        variable : str
            variable sur laquelle on fait l'agrégation
        L1 : list
            liste des variables sur laquelle on calcule la moyenne
        L2 : list
            liste des variables sur laquelle on somme les valeurs
        L3 : list 
            liste des variables qu'on retire de la table
        L4 : list
            liste des variables qui ne changent pas sur une agrégation
        
        Examples
        --------
        '''
        self.variable=variable
        self.L1=L1
        self.L2=L2
        self.L3=L3
        self.L4=L4


    def transfo(self,table:Table):
        '''

        Description longue
        ------------------
        

        Attributes
        ----------
    

        Examples
        --------
        '''
        def aux(agreg):
            tab=Table((self.var), [])


            for i in range (len(agreg)):
                L=[] #on crée pour chaque agrégation, la liste de data pour l'agrégation.
                l_indice=self.l_index(self.variable, agreg[i]) #retourne une liste avec les index des individus dans l'agregation i
                le=len(l_indice)#nombre d'individu pour chaque agregation
                for j in range (len(table.var)):
                    if (table.var)[j] in self.L1:
                        m=0
                        for k in range (le):
                            m+=(table.data)[l_indice[k]][j]
                        m=m/len(l_indice)
                        L.append(m)
                    elif (table.var)[j] in self.L2:
                        S=0
                        for k in range (le):
                            S+=(table.data)[l_indice[k]][j]
                        L.append(S)
                    elif (table.var)[j] in self.L4:
                        value=(table.data)[l_indice[0]][j] #on prend la première valeur de la variable pour cet agreg car elle ne change pas pour L4
                        L.append(value)

                (tab.data).append(L+agreg[i])

            #L3 variables qu'on retire de la table
            for i in range (len(self.L3)):
                tab.enlev_var(self.L3[i])
        
            return tab
        #fin fonction auxiliaire
        
        if self.variable=="National":
            agreg=[France]
        elif self.variable in table.var:
            agreg=list(set(table.extraire_var(self.variable))) #Pour séléctionner les valeurs distinctes de la variable d'agregation
        else : 
            raise Exception("La variable saisie n'est pas une variable possible d'agrégation")
        
        return aux(agreg)

        