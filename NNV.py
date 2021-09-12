import numpy as np
import random 




"""""This is the NNV ALGORTIHM coded in a normal way """
def swapPositions(l, pos1, pos2):
    l[pos1], l[pos2] = l[pos2], l[pos1]
    return l

def latlong(n):
    x = []
    y= []
    random.seed(n)
    for i in range(n):
        a = random.uniform(0,18)
        b = random.uniform(0,36)
        x.append(a)
        y.append(b)
    return x,y
 
def matdist(n):
    a = latlong(n)
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

    
def minpath(mat):
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

    
def swapR(x) :
    mindis= np.Inf
    c = np.zeros((len(x),len(x)))
    his = []
    minhis = []
    valhis = []
    L = []
    k=0
    while k < len(x) :
        new_order = [i for i in range(len(x))]
        new_order = swapPositions(new_order, 0, k)
        his.append(new_order)
        c = [[x[i][j] for j in new_order] for i in new_order]
        new_order.append(new_order[0])
        d = np.array(c)
        c = minpath(d)
        valhis.append(c[0])
        L.append((c[1],new_order))  
        k = k +1
        if c[0] < mindis :
                matt = d
                mindis = c[0]
                new_order2 = c[1]
                minhis.append(new_order2)
        else :
            continue
    his.append(new_order2)
    return matt,new_order2,mindis,his,minhis,valhis,L
