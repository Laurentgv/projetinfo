import datetime
from Table import Table

class Fenetrage:
    '''
    Sélection des données sur une période temporelle
    '''
    def __init__(Table):
        super().__init__()

    def fun(self):
        '''
        '''
        print("Saisir date de début au format yyyymmdd")
        date_debut=input()
        print("Saisir heure de début au format hhmmss")
        heure_debut=input()
        print("Saisir date de fin au format yyyymmdd")
        date_fin=input()
        print("Saisir heure de fin au format hhmmss")
        heure_fin=input()

        anneed=date_debut[0:4]
        moisd=date_debut[4:6]
        jourd=date_debut[6:8]
        hd=heure_debut[0:2]
        md=heure_debut[2:4]
        sd=heure_debut[4:6]

        anneef=date_fin[0:4]
        moisf=date_fin[4:6]
        jourf=date_fin[6:8]
        hf=heure_fin[0:2]
        mf=heure_fin[2:4]
        sf=heure_fin[4:6]

        debut=datetime.datetime(anneed,moisd,jourd,hd,md,sd)
        fin=datetime.datetime(anneef,moisf,jourf,hf,mf,sf)

        assert(debut<=fin)
        indice = self.ind("date")
        data=self.data
        L=[]
        for i in range (len(data)):

            date=data[i][indice]
            annee=date[0:4]
            mois=date[4:6]
            jour=date[6:8]
            heure=date[8:10]
            min=date[10:12]
            sec=date[12:14]

            actuel=datetime.datetime(annee,mois,jour,heure,min,sec)

            if (actuel>=debut) and (actuel<=fin): 
                L.append(data[i])
        self.data=L
        return Table((self.var),L)



