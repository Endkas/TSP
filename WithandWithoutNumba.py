import os
os.chdir("C:\\Users\\Endrit\\Desktop\\Master Finance\\2nd Semster\\Programming\\ProjectVF\\")
print("Current working directory: {0}".format(os.getcwd()))
from NNVnumba import *
from NNV import*
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
from time import time



tnumba = []
tfunc = []
for i in range(10,301):
    print(i)
    a = matdistNUMBA(i)
    b = matdist(i)
    start = time()
    swapRNUMBA.recompile() # we recompile the function each time
    swapRNUMBA(a[0])
    end = time()
    tnumba.append(end-start)
    
    start = time()
    swapR(b[0])
    end = time()
    tfunc.append(end - start)
    

plt.plot(tnumba, linestyle="-", color="lightblue", linewidth="0.9",label='with numba')
plt.plot(tfunc,linestyle="solid", color="cadetblue", linewidth="0.9",label='without numba')
plt.xlabel('Number of cities')
plt.ylabel('Time (in secs) of NNV algorithm')
plt.xlim(10,300)
plt.xticks(np.arange(10, 300, step=50),labels=(np.arange(10, 300, step=50)))
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('Numba300Cities.png', dpi=1400)

