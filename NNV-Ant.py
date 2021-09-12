import os
os.chdir("C:\\Users\\Endrit\\Desktop\\Master Finance\\2nd Semster\\Programming\\ProjectVF\\")
print("Current working directory: {0}".format(os.getcwd()))
from ClassCities import Cities
from ClassNNV import NNV
from ClassAnt import Ant
import numpy as np
import random 
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from time import time



tnnv = []
tant = []
tant30 = []



for n in range(20,61) :
    print(n)
    start = time()
    nnv = NNV(n)
    nnv.swapR()
    end = time()
    tnnv.append(end-start)
        
    start = time()
    ant = Ant(n)
    ant.desir()
    ant.Sim(maxfrac=1)
    end = time()
    tant.append(end - start)
    
    start = time()
    ant = Ant(n)
    ant.desir()
    ant.Sim()
    end = time()
    tant30.append(end - start)

    

x = np.arange(20,61,step=1)
plt.plot(x,tnnv, linestyle="solid", color="lightblue", linewidth="0.9",label='Nearest Neighbor')
plt.plot(x,tant,linestyle="-.", color="cadetblue", linewidth="0.9",label='Ant colony max iter = 100%')
plt.plot(x,tant30,linestyle="--", color="darkturquoise", linewidth="0.9",label='Ant colony max iter = 30%')
plt.xlabel('Number of cities')
plt.ylabel('Time (in secs) of NNV algorithm')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('nnv-ant50.png', dpi=1400) #Figure 9 of our paper



""""" this part of the code is to see how the heuristic algorithms
     do again eacher other,which one found the smallest minimum path """
nnvl = 0
antl = 0
draw = 0
for n in range(10,31) :
    print(n)
    for i in range(101):    
        nnv = NNV(n,i)
        nnv.swapR()
        a = np.round(nnv.mindis,12)
    
        ant = Ant(n,i)
        ant.desir()
        ant.Sim(maxfrac=1) # we only did with number of ants equal number of cities
        b = np.round(ant.bestTests,12)
        if a < b: 
            nnvl += 1
        elif a > b :
            antl +=1
        else :
            draw += 1

resultNNV = np.sum(nnvl)
resultANT = np.sum(antl)
resultDRAW = np.sum(draw)
    
total = resultNNV + resultANT + resultDRAW

x = [resultNNV ,resultANT , resultDRAW]/total 
""" x[0] will tell the percentage of time when NNV find a smaller distance
     than the ACO
     x[1] when the ACO find a smaller distance
     x[2] when they find the same distance
     
     """
