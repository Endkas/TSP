import os
os.chdir("C:\\Users\\Endrit\\Desktop\\Master Finance\\2nd Semster\\Programming\\ProjectVF\\")
print("Current working directory: {0}".format(os.getcwd()))

from ClassCities import Cities
from AniTSP import animateTSP
import numpy as np
import random 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
plt.style.use('ggplot')


class NNV(Cities):
    """
    Our algorithm is a version of Neirghest Neighbor
    example of utilisation :
    a = NNV(200) #200 cities will be generated
    a.minpath() , here it is just applying the NNV one time
    a.swapR(), here we apply the NNV to each city being the starting city

    
    """
    
    def __init__(self,n,seed=10):
        """
        iherit matrix of distances and n from class Cities
        """
        Cities.__init__(self,n,seed)
        self.path = []
        self.res = 0
    
    def swapPositions(self,l, pos1, pos2):
        """
        method to swap position in a list
        
        """
        l[pos1], l[pos2] = l[pos2], l[pos1]
        return l
        
    def minpath(self,a=None):
        """
        this is the conventional NN algorithm applied to the matrix
        
        """
        x = self.mat if a is None else a
        v = np.zeros((len(x),len(x)))
        r = 0
        c = 0
        minn = 100
        last = 0
        ii = [i for i in range(len(x))] # see ii as the list of departure cities
        jj = ii.copy()[1:] #see jj as the list of arrival cities
        path = [] # the path from city to city
        k = 0
        for i in ii:
            k = k + 1
            if k  == len(x): # all cities have been visited
                break
            else :
                for j in jj:
                    if (x[i,j] <  minn) and (x[i,j] != 0) and (x[i,j] !=last) : 
                        minn = x[i,j]
                        r = i
                        c = j
                last = x[r,c]
                jj.remove(c)
                ii.remove(c)
                ii.insert(k,c)
                path.append(c)
                v[r,c] = 1
                minn = 100
        v[j,0] = 1 # go back to starting cities           
        path.insert(0,0)
        path.append(path[0])
        res = np.sum(v*x)
        if a is None :
            self.path = path
            self.res = res    
        return res,path
    
    
    def swapR(self) :
        """ 
        With this method we apply the NN to each city
        being the first city.
        We will swap the order, so that each city one time the starting city.
        We also have to change the matrix of distances.
        
        
        """
        x = self.mat
        self.mindis= np.Inf
        c = np.zeros((len(x),len(x)))
        self.his = [] # historic of path
        self.minhis = [] # historic of minimum values
        self.valhis = [] # historic of the lenght of path
        self.L = [] # tuple of the path and the new order
        k=0
        while k < len(x) :
            new_order = [i for i in range(len(x))]
            new_order = self.swapPositions(new_order, 0, k) #we swap each line to make each city being the starting one
            self.his.append(new_order)
            c = [[x[i][j] for j in new_order] for i in new_order] #as we change order,we also change matrix of distances in consequence
            new_order.append(new_order[0])
            d = np.array(c)
            c = self.minpath(d) 
            self.valhis.append(c[0])
            self.L.append((c[1],new_order))  
            k = k +1
            if c[0] < self.mindis :
                self.matt = d
                self.mindis = c[0]
                self.new_order2 = c[1]
                self.minhis.append(self.new_order2)
            else :
                continue
        self.his.append(self.new_order2)
        return self.matt,self.new_order2,self.mindis,self.his,self.minhis,self.valhis,self.L
    
    def generalpaths(self):
        """To compute the NN for each city being the first city,we swapped
        the order of the matrix. And from that we got a path, but the path
        was for the matrix dispostion. Therefore, we need to get a general path,
        i.e that each path is exprimed with the same matrix.
        """
        self.GG = []
        for i in self.L :
            G = []
            for j in i[0][:-1]:
                G.append(i[1][j])
            self.GG.append(G)
        return self.GG
    
    def sortpaths(self):
        """Ww sort path by minimum length found
        and keep only the 10% smallest path"""
        self.generalpaths()
        self.LL = [i for _,i in sorted(zip(self.valhis,self.GG))]
        if self.n >= 10 :
            self.LL = self.LL[:int(len(self.LL)/10)]
        else :
            self.LL = self.LL[:1]
        return self.LL
    
    def nn(self):
        """with this method we look at the 10% smallest path,
        and for each city, we looked at the neighbor on the right and left.
        After this method we will have a dictionnary wih each city (key) and their respecitve
        nearest neighbor for the 10% smallest path found by the NN algorihtm.
        """
        self.sortpaths() 
        self.NN = dict.fromkeys((range(self.n)))
        e = 0
        for i in self.LL :
            e = e + 1
            k = -1
            if e == 1 :               
                for j in i:
                    k = k +1 
                    if j == i[0] :
                        self.NN[j] = [i[1],i[-1]]
                    elif j == i[-1]:
                        self.NN[j] = [i[k-1],i[0]]
                    else :
                        self.NN[j] = [i[k-1],i[k+1]]
                print(self.NN)
            else :
                for j in i:
                    k = k +1 
                    if j == i[0] :
                        self.NN[j].append(i[1])
                        self.NN[j].append(i[-1])
                    elif j == i[-1]:
                        self.NN[j].append(i[k-1])
                        self.NN[j].append(i[0])
                    else :
                        self.NN[j].append(i[k-1])
                        self.NN[j].append(i[k+1])
        for o in range(self.n):
            self.NN[o] = list(set(self.NN[o]))
            
        return self.NN
    
    def minpathNN(self):
        """
        This method goes with the method sprtpath and nn,
        We had the idea to look at the 10% smallest path found by NN
        and from that reaply the NN algorithm but with first looking only at
        the closet neighbor found in the 10% smallest path.
        We didnt talk about this method in the report because,this method was
        giving us the same results as the SwapR method. It was not realy efficace
        in finding a smaller path than SwapR.
        
        """
        self.nn()
        x = self.mat
        v = np.zeros((len(x),len(x)))
        r = 0
        c = 0
        minn = 100
        last = 0
        w = 0
        self.res2 = np.inf
        self.path2 = []
        ii = [i for i in range(len(x))]
        while w < self.n :
            iii = ii.copy()
            iii = self.swapPositions(iii, 0, w)  
            jj = iii.copy()[1:]
            path2 = []
            k = 0
            for i in iii:
                k = k + 1
                if k  == len(x):
                    break
                else :
                    for j in self.NN[i]:
                        if (x[i,j] <  minn) and (x[i,j] != 0) and (x[i,j] !=last) and j in jj :
                            minn = x[i,j]
                            r = i
                            c = j
                        else :
                            for j in jj :
                                if (x[i,j] <  minn) and (x[i,j] != 0) and (x[i,j] !=last)  :
                                    minn = x[i,j]
                                    r = i
                                    c = j
                    last = x[r,c]
                    jj.remove(c)
                    iii.remove(c)
                    iii.insert(k,c)
                    path2.append(c)
                    v[r,c] = 1
                    minn = 100
                    
            v[j,iii[0]] = 1            
            path2.insert(0,iii[0])
            path2.append(path2[0])
            res2 = np.sum(v*x)
            w = w + 1
            if res2 < self.res2 :
                self.res2 = res2
                self.path2 = path2
            else :
                continue
        return self.res2,self.path2
    def __str__(self):
        return "Minpath is :" + str(self.new_order2) + "  and has a length of : " + str(self.mindis)
    

def animateTSPNNV(a,fps = 3,dpi=600):
    """give an instance of the NNV Class"""
    x = a.x
    y = a.y
    history = a.LL[0]
    points = a.coord
    n = a.n
    fig, ax = plt.subplots()
    def init():
        ax.scatter(x, y, marker = 'o',color="c",s=40)
        extra_x = (max(x) - min(x)) * 0.05
        extra_y = (max(y) - min(y)) * 0.05
        ax.set_xlim(min(x) - extra_x, max(x) + extra_x)
        ax.set_ylim(min(y) - extra_y, max(y) + extra_y)
    def update(frame):
        ''' for every frame update the solution on the graph '''
        if frame == len(history)-1 :
            k = history[frame]
            kk = history[0]
        else :
            k = history[frame]
            kk = history[frame+1]
            
        x1 = points[k][0]
        y1 = points[k][1]
        x2 = points[kk][0]
        y2 = points[kk][1]
        X = [x1 , x2]
        Y = [y1 , y2]
        if frame == len(history)-1 :
            ax.plot(X,Y, linestyle="solid", color="lightblue", linewidth="1")
        else :
            ax.plot(X,Y, linestyle="solid", color="c", linewidth="0.5")
    
        ax.set_title('Nearest neighbor available algorithm')

        return ax

    ''' animate precalulated solutions '''
    
    ani = FuncAnimation(fig, update, frames= range(0, len(history)),
                        init_func=init, interval=100, repeat=False,blit =False)
    ani.save('Animation'+str(a.__class__.__name__)+'-'+str(n)+'cities'+'.gif',writer='Pillow',fps=fps,dpi=dpi)
    
    plt.show()

#a = NNV(200)
#a.minpath() , here it is just applying the NNV one time
#a.swapR(), here we apply the NNV to each city being the starting city
#a.minpathNN()
#b = animateTSPNNV(a)