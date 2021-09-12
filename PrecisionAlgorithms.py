#pip install python_tsp
from python_tsp.exact import solve_tsp_dynamic_programming
import os
os.chdir("C:\\Users\\Endrit\\Desktop\\Master Finance\\2nd Semster\\Programming\\ProjectVF\\")
print("Current working directory: {0}".format(os.getcwd()))
from ClassCities import Cities
from ClassNNV import NNV
from ClassAnt import Ant
import numpy as np





nnvprec = []
antprec = [] 
antnprec = [] 
bfprec = []
for n in range(5,8) :
    stat = 0
    print("this is :",n)
    for i in range(1,100) :
        nnv = NNV(n,i)
        nnv.swapR()
        ant = Ant(n,i)
        ant.desir()
        ant.Sim() # 30% of the number of cities of ants are generate by default
        a = Cities(n,i)
        distance_matrix = a.mat
        permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
        bfprec.append(distance)
        nnvprec.append(nnv.mindis)
        antprec.append(ant.bestTests)
        antt = Ant(n,i)
        antt.desir()
        antt.Sim(maxfrac=1) #here we generate as many ants as the number of cities
        antnprec.append(antt.bestTests)
        
nnvpreC = np.round(np.array(nnvprec),12) # here we round to 12 decimals
antpreC = np.round(np.array(antprec),12)
antnpreC = np.round(np.array(antnprec),12)
bfpreC = np.round(np.array(bfprec),12)
nnvpreC = (nnvpreC-bfpreC)/bfpreC
antpreC = (antpreC-bfpreC)/bfpreC
antnpreC = (antnpreC-bfpreC)/bfpreC

meanNNV = np.mean(nnvpreC)
meanANT = np.mean(antpreC)
meanNANT = np.mean(antnpreC)

print("this is the average precisions of the NNV algorithm over 100 iterations from 5 to 20 ciites :",1-meanNNV)
print("this is the average precisions of the Ant algorithm with number of ants = 0.3n over 100 iterations from 5 to 20 ciites :",1-meanANT)
print("this is the average precisions of the Ant algorithm  with number of ants = n over 100 iterations from 5 to 20 ciites :",1-meanNANT)

#this is the average precisions of the NNV algorithm over 100 iterations from 5 to 20 ciites : 0.9618642998308147
#this is the average precisions of the Ant algorithm with number of ants = 0.3n over 100 iterations from 5 to 20 ciites : 0.8413103734128827
#this is the average precisions of the Ant algorithm with number of ants = n over 100 iterations from 5 to 20 ciites : 0.9688680799305202



