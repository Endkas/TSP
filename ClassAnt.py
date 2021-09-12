import os
os.chdir("C:\\Users\\Endrit\\Desktop\\Master Finance\\2nd Semster\\Programming\\ProjectVF\\")
print("Current working directory: {0}".format(os.getcwd()))

from ClassCities import Cities
#from AniTSP import animateTSP
import numpy as np
import random 
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from random import randint as r
import math


class Ant(Cities):
    def __init__(self,n,seed=10):
        Cities.__init__(self,n,seed)
        self.pheromone0 = 10 * 1 / (self.n * np.mean(self.mat))
        phero = [self.pheromone0]*self.n
        self.pheromone =  [phero for i in range(self.n)] # Pheromone matirx
        self.evap = 0.5 # Evaporation rate
        self.alpha = 1.0  # Pheromone weight to desirability
        self.beta = 1.0  # Desirability weight to pheromone
        self.desirability = []   # desirability of each edge
        self.bestTests = np.inf
        self.bestTour = []
        self.besthis = []
        self.pherohis = []
        
    def indices(self,a, func):
        return [i for (i, val) in enumerate(a) if func(val)]

    def desir(self):
        # desirability doesn't change so may as well apply beta when calculating
        for i in range(self.n):
            s = []
            for j in range(self.n):
                if self.mat[i][j] != 0:
                    s.append(math.pow(1/self.mat[i][j], self.beta))
                else:
                    s.append(math.inf)
            self.desirability.append(s)

    #create a colony, with the different ant batches
    def Colony(self):
        antNo = self.n # we initilaze 2n ants
        self.colony = {"ant": [],"besttour": {"tour": [],"test": [] } }
        for i in range(antNo):
            s = {"tour": [] }
            initial_node = r(0 , self.n-1) # select a random node
            s["tour"].append(initial_node)
            self.colony["ant"].append(s)   
            while len(s["tour"]) != self.n : # to choose the rest of nodes
                currentNode =  self.colony["ant"][i]["tour"][len(self.colony["ant"][i]["tour"])-1]#current node of an ant
                d1=[math.pow(ii, self.alpha) for ii in self.pheromone[currentNode][:]]
                d2=[jj for jj in self.desirability[currentNode][:]]
                P_allNodes = []
                # JA: since we're only updating for the same index, no need to iterate over both
                # JA: both should be the same length anyway
                for k in range(len(d1)):
                    P_allNodes.append(d1[k] * d2[k])
                for x in self.colony["ant"][i]["tour"]:
                    P_allNodes[x] = 0  # assigning 0 to all the nodes visited so far
                P = [xx/np.nansum(P_allNodes) for xx in P_allNodes]
                cumsumP = np.cumsum(P)#assign a cumulative sum with the probabilities
                r1 = random.random()#make the ant pick a random number
                nextNode = self.indices(cumsumP, lambda x: x >= r1)#based on the random number, pick the next city
                nextNode = nextNode[0]
                xc = self.colony["ant"][i]["tour"]
                xc.append(nextNode)#add the new city to the memory function
                self.colony["ant"][i]["tour"] = xc
    
            # complete the tour
            xcc = self.colony["ant"][i]["tour"]
            xcc.append(self.colony["ant"][i]["tour"][0])
            self.colony["ant"][i]["tour"] = xcc 
        return self.colony
    
    def Test (self,tour):
        self.tour = tour
        self.test = 0
        for i in range(len(self.tour)-1):
            currentNode = tour[i]
            nextNode = tour[i+1]
            self.test = self.test + self.mat[currentNode][nextNode]
        return self.test
    
    
    def updatePheromone(self): # Update the pheromone matrix.
        nodeNo = len(self.colony["ant"][1]["tour"])
        antNo = len(self.colony["ant"][:])
        for i in range(antNo):  # for each ant
            for j in range(nodeNo-1):  # for each node in the tour
                currentNode = self.colony["ant"][i]["tour"][j]
                nextNode = self.colony["ant"][i]["tour"][j+1]
                self.pheromone[currentNode][nextNode] = self.pheromone[currentNode][nextNode] + 1 / self.colony["ant"][i]["test"]#updte the pheromone based on the ant's performance
                self.pheromone[nextNode][currentNode] = self.pheromone[nextNode][currentNode] + 1 / self.colony["ant"][i]["test"]#do it in both direction
        return self.pheromone
    
    
    def drawGraph(self):#plot the iterations
        for i in range(self.n-1):
            for j in range(i+1, self.n):
                x1 = self.x[i]
                y1 = self.y[i]
    
                x2 = self.x[j]
                y2 = self.y[j]
    
                X = [x1 , x2]
                Y = [y1 , y2]
    
                plt.plot(X, Y, linestyle="solid", color="black", linewidth="0.03")
            plt.scatter(self.x, self.y, marker = 'o',color="c",s=40)        
        for i in range(self.n-1):
            for j in range(i+1, self.n):
                x1 = self.x[i]
                y1 = self.y[i]
    
                x2 = self.x[j]
                y2 = self.y[j]
    
                X = [x1 , x2]
                Y = [y1 , y2]
    
                plt.plot(X, Y, linestyle="solid", color="black", linewidth="0.03")
            plt.scatter(self.x, self.y, marker = 'o',color="c",s=40)
     
    
    def drawBestTour(self):#we want to highlight the best tour
        besthis = []
        besttour = self.colony["besttour"]["tour"]
        for i in range(len(besttour)-1):
            currentNode = besttour[i]
            nextNode =  besttour[i+1]
            x1 = self.x[currentNode]
            y1 = self.y[currentNode]
            x2 = self.x[nextNode]
            y2 = self.y[nextNode]
    
            X = [x1 , x2]
            Y = [y1, y2]
            besthis.append((X,Y))
            plt.plot(X, Y, linestyle="solid", color="c", linewidth="0.5")
        self.besthis.append(besthis)
        plt.scatter(self.x, self.y, marker = 'o',color="c",s=40)
        plt.xticks(labels = None)
        plt.xticks(labels = None)
        plt.title('Best tour of iteration ' + str((self.t+1)))

        #create a graph with the evolution of the pheromone throughout the iteration, highlight the key paths
    def GraphPheromone(self):
        maxPhe = np.max(self.pheromone[:])
        minPhe = np.min(self.pheromone[:])
        tt = [j-minPhe for j in self.pheromone]
        pheromone_normalized = [i/(maxPhe - minPhe) for i in tt]
        self.pherohis.append(pheromone_normalized)
        for i in range(self.n-1):
            for j in range(i+1, self.n):
                x1 = self.x[i]
                y1 = self.y[i]
    
                x2 = self.x[j]
                y2 = self.y[j]
    
                X = [x1 , x2]
                Y = [y1 , y2]
                
                plt.plot(X, Y, linestyle="solid", color=[0, 0, (1-pheromone_normalized[i][j]),  pheromone_normalized[i][j]], linewidth=3*pheromone_normalized[i][j] + 0.7)
        plt.scatter(self.x, self.y, marker = 'o',color="c",s=40)
        plt.xticks(labels = None)
        plt.xticks(labels = None)
        plt.title('All Pheromones')

    
    def Sim(self,graph = False,outmsg=False,maxfrac=0.3):
        maxiter = int(self.n*maxfrac) # here if maxfrac = 1 we generate a number of ants which is equal to the number of cities
        for t in range(maxiter):# Create Ants
            self.t = t # usefull to drawgraph to see at which iterations we are                
            self.Colony()
            allAntsTests = []
            for i in range(self.n):
                self.colony["ant"][i]["test"] = self.Test(self.colony["ant"][i]["tour"])
                # Find the best ant (besttour)
                allAntsTests.append(self.colony["ant"][i]["test"])
        
            minVal = np.min( allAntsTests )
            minIndex = self.indices(allAntsTests, lambda x: x == minVal)
        
            if minVal < self.bestTests:
                self.bestTests = self.colony["ant"][minIndex[0]]["test"]
                self.bestTour = self.colony["ant"][minIndex[0]]["tour"]
        
            self.colony["besttour"]["tour"] = self.bestTour
            self.colony["besttour"]["test"] = self.bestTests
        
            # JA: Evaporate before strengthening the trails
            for n in range(0, len(self.pheromone)):
                self.pheromone[n] = [i * (1 - self.evap) for i in self.pheromone[n]]
        
            # Update phromone matrix
            self.pheromone = self.updatePheromone()
            if outmsg :
                outmsg = [ 'Iteration #' + str(t) + ' Shortest length = ' + str(self.colony["besttour"]["test"]) ]
                print(outmsg)
                   # Visualize best tour and pheromone concentration
            if graph :    
                plt.subplot(1, 2,1)
                self.drawBestTour()
                plt.subplot(1, 2, 2)
                self.GraphPheromone()
                plt.savefig(str(self.__class__.__name__)+'-'+str(self.n)+'cities'+'iter'+str((t+1))+'.png',dpi=1400)
                plt.show()


#anime the iterations results
def animateTSPant(a,fps = 1.3,dpi=400):
    """anime the iterations results
    you need to create an instance ant,then apply the method desir,colony and sim
    here is an example :
        b = Ant(50)
        b.desir()
        b.Colony()
        b.Sim(True)
        end = animateTSPant(b,fps=0.6,dpi=1400)
        
        """
    
    x = a.x
    y = a.y
    history = a.besthis
    n = a.n
    fig, (ax1, ax2) = plt.subplots(1, 2)
    def init():
        ax1.scatter(x, y, marker = 'o',color="c",s=40)
        ax2.scatter(x, y, marker = 'o',color="c",s=40)
        extra_x = (max(x) - min(x)) * 0.05
        extra_y = (max(y) - min(y)) * 0.05
        ax1.set_xlim(min(x) - extra_x, max(x) + extra_x)
        ax2.set_xlim(min(x) - extra_x, max(x) + extra_x)
        ax1.set_ylim(min(y) - extra_y, max(y) + extra_y)
        ax2.set_ylim(min(y) - extra_y, max(y) + extra_y)
    def update(frame):
        ''' for every frame update the solution on the graph '''
        ax1.lines = []
        ax2.lines = []# this will clear the lines of last graph
        xx = []
        yy = []
        for i in history[frame]:
            xx = i[0] 
            yy = i[1]
            ax1.plot(xx,yy, linestyle="solid", color="c", linewidth="0.5")
        ax1.set_title('Best tour of iteration ' + str((frame+1)))
            
        for i in range(a.n-1):
            for j in range(i+1, a.n):
                x1 = x[i]
                y1 = y[i]
                x2 = x[j]
                y2 = y[j]
                X = [x1 , x2]
                Y = [y1 , y2]
                pheromone_normalized = a.pherohis[frame]
                ax2.plot(X, Y, linestyle="solid", color=[0, 0, (1-pheromone_normalized[i][j]),  pheromone_normalized[i][j]], linewidth=3*pheromone_normalized[i][j] + 0.7)
        ax2.set_title('All Pheromones')
        return ax1

    ''' animate precalulated solutions '''

    ani = FuncAnimation(fig, update, frames= range(0, len(history)-1),
                        init_func=init, interval=100, repeat=False,blit =False)
    ani.save('Animation'+str(a.__class__.__name__)+'-'+str(n)+'cities'+'.gif',writer='Pillow',fps=fps,dpi=dpi)
    

    plt.show()

#b = Ant(50,seed=2)
#b.desir()
#b.Colony()
#b.Sim(True,maxfrac=1)
#end = animateTSPant(b,fps=0.6,dpi=1400)

