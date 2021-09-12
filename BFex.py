import numpy as np
import itertools
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import pandas as pd
"""""Class to solve the TSP for our little example with the 10 biggest cities in CH """
class bftsp(object):
    def __init__(self,mat):
        self.matkm = mat
        self.n = len(mat)

    def bf(self,a= True) :
        if a == True :
            mat = self.matkm
        else :
            mat = self.mat   
        minLength = np.inf
        for tour in itertools.permutations(list(range(1,self.n))):
            fr = 0
            length = 0
            count = 0
            while count < self.n-1:
                to = tour[count]
                length += mat[fr][to]
                fr = to
                count += 1
            length += mat[fr][0]
            if length < minLength:
                minLength = length
                minTour = tour
                minTour = (0,) + minTour + (0,)
        if a == True :
            self.minLengthkm = minLength
            self.minTourkm =  minTour
        else :
            self.minLength = minLength
            self.minTour = minTour         
    
    def matdist(self,coords):
        self.coord = coords
        self.mat = np.zeros((self.n,self.n))
        for i in range(self.n):
            for j in range(i+1,self.n):
                lon = (self.coord[i][0]-self.coord[j][0])**2
                la = (self.coord[i][1]-self.coord[j][1])**2
                self.mat[i,j] = (la + lon)**0.5
                self.mat[j,i] = self.mat[i,j]
        return self.mat
    
    def __str__(self):
        return "Minpath is :" + str(self.minTour) + "  and has a length of : " + str(self.minLength)


