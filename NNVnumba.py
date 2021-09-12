import numpy as np
from numba import jit
import random 
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import os

os.chdir("C:\\Users\\Endrit\\Desktop\\Master Finance\\2nd Semster\\Programming\\ProjectVF\\")
print("Current working directory: {0}".format(os.getcwd()))

"""""This is the NNV ALGORTIHM coded in a normal way with NUMBA """
@jit(nopython=True)
def swapPositionsNUMBA(l, pos1, pos2):
    l[pos1], l[pos2] = l[pos2], l[pos1]
    return l

@jit(nopython=True)
def latlongNUMBA(n):
    x = []
    y= []
    random.seed(n)
    for i in range(n):
        a = random.uniform(0,18)
        b = random.uniform(0,36)
        x.append(a)
        y.append(b)
    return x,y

@jit(nopython=True)    
def matdistNUMBA(n):
    a = latlongNUMBA(n)
    x= a[0]
    y = a[1]
    coord = []
    mat = np.zeros((n,n))
    for i in range(n):
        coord.append((x[i],y[i]))
        for j in range(i+1,n):
            la = (x[i]-x[j])**2
            lon = (y[i]-y[j])**2
            mat[i,j] = (la + lon)**0.5
            mat[j,i] = mat[i,j]
    return mat,coord

@jit(nopython=True)     
def minpathNUMBA(mat):
    x = mat
    v = np.zeros((len(x),len(x)))
    r = 0
    c = 0
    minn = 100
    last = 0
    ii = [i for i in range(len(x))]
    jj = ii.copy()[1:]
    path = []
    k = 0
    for i in ii:
        k = k + 1
        if k  == len(x):
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
    v[j,0] = 1            
    path.insert(0,0)
    path.append(path[0])
    res = np.sum(v*x)
    return res,path

    
@jit(nopython=True)
def swapRNUMBA(x) :
    mindis= np.Inf
    c = np.zeros((len(x),len(x)))
    #his = []
    #minhis = []
    #valhis = []
    L = []
    k=0
    while k < len(x) :
        new_order = [i for i in range(len(x))]
        new_order = swapPositionsNUMBA(new_order, 0, k)
        #his.append(new_order)
        c = [[x[i][j] for j in new_order] for i in new_order]
        new_order.append(new_order[0])
        d = np.array(c)
        c = minpathNUMBA(d)
        #valhis.append(c[0])
        L.append((c[1],new_order))  
        k = k +1
        if c[0] < mindis :
                matt = d
                mindis = c[0]
                new_order2 = c[1]
                #minhis.append(new_order2)
        else :
            continue
    #his.append(new_order2)
    return matt,new_order2,mindis #,his,minhis,valhis,L






"""
The coded used to plot the figure with 5000 cities
from time import time 
a = matdistNUMBA(5000)
n = 5000 it took : 4343.56009888649 (seconds)
swapRNUMBA.recompile()
start = time()
w = swapRNUMBA(a[0])
print("it took :",time()-start)
#n = 5000 it took : 4343.56009888649 

b = latlongNUMBA(5000)
x = b[0]
y = b[1]
history = w[1]
points = a[1]
n = len(x)
fig, ax = plt.subplots()
ax.scatter(x, y, marker = 'o',color="darkgray",s=1)
extra_x = (max(x) - min(x)) * 0.05
extra_y = (max(y) - min(y)) * 0.05
ax.set_xlim(min(x) - extra_x, max(x) + extra_x)
ax.set_ylim(min(y) - extra_y, max(y) + extra_y)
ax.set_title('Nearest neighbor available algorithm')
for frame in range(0,len(history)):
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
    ax.plot(X,Y, linestyle="solid", color="c", linewidth="0.5")
plt.tight_layout()
plt.show()
fig.savefig('Graphbb-'+str(n)+'cities'+'.png',dpi=1400)

"""
