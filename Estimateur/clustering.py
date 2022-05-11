from estimateur import Estimateur
from random import randrange
import numpy as np

class Clustering(Estimateur):
    '''Estimateur(?), on code les deux méthodes de clustering'''

    def __init__(self, data):
        '''data est du type dataframe ie un tableau les observations en lignes et les variables en colonne. 
        Il faut que toutes les données soient numériques -> faut il une méthode pour transformer les qualitative en quantitative ?'''
        self.data=data

    def k_means(self, k):
        '''Faut il le coder soit meme ou bien utiliser un package ?
        On va utiliser les numpy arrays, qui ressemblent beaucoup aux dataframe de R (?)
        '''
        data=np.asarray(self.data)
        n=len(self.data)
        #On veut rajouter une colonne cluster qui donne à chaque individu son numéro de cluster (entre 1 et k)
        cluster_nb=[0]*len(self.data)
        for i in range(len(cluster_nb)):
            cluster_nb[i]=randrange(k)
        np.concatenate(data, np.asarray(cluster_nb))

        #On veut créer les k cluster. Est ce que on les prends parmis les individus ? Ou au hasard ?
        for i in range(k):

            cluster_pos=np.asarray(data[randrange(n)],)
        

        
