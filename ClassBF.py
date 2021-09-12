import os
os.chdir("C:\\Users\\Endrit\\Desktop\\Master Finance\\2nd Semster\\Programming\\ProjectVF\\")
print("Current working directory: {0}".format(os.getcwd()))
from ClassCities import Cities
import numpy as np
import itertools
import math


class BFtsp(Cities):
    def __init__(self,n,seed=10):
        """
        This is the class of the Brute Force algorithm to solve the TSP.This class
        inherits the matrix distances and coordinates of the Superclass Cities.
        The complexity of this algorithm is O((n-1)!)
        

        Parameters
        ----------
        n : Number of cities you want to generate
        
        seed : The seed you want to use for random.seed(seed=seed), optional.
        The default is 10. The seed is by default the same for all the different classes,so
        that with the same number of cities, the matrix of distances is the same.
        With that we can compare results of different algorithms as it exactly the same numbers in the
        distances'matrix.
    

        """
        Cities.__init__(self,n,seed) 
        self.minLength = np.inf
        self.minTour = []
        self.his = []
        self.valhis = []
    
        
    def bf(self) :
        """
        

        Returns
        -------
        minLength
            This is the length of the smallest path.
        minTour
            This is a list which give the path, from town to town.

        """
        for tour in itertools.permutations(list(range(1,self.n))):
            self.his.append((0,) + tour + (0,))
            fr = 0
            length = 0
            count = 0
            while count < self.n-1:
                to = tour[count]
                length += self.mat[fr][to]
                fr = to
                count += 1
            length += self.mat[fr][0]
            self.valhis.append(length)
            if length < self.minLength:
                self.minLength = length
                self.minTour = tour
                self.minTour = (0,) + self.minTour + (0,)
        self.his.append(self.minTour)
        return self.minLength,self.minTour
    
    def __str__(self):
        return "Minpath is :" + str(self.minTour) + "  and has a length of : " + str(self.minLength)



#a = BFtsp(9)
#a.bf()

    