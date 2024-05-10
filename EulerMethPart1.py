import matplotlib.pyplot as plt
import numpy as np

def fonction(a,x0,y,z,h):
    L1=[x0]
    L2=[y]
    i=x0
    pas=(z-i)/h
    while i<h:
        x0=x0+pas
        y=y+(a*y)*pas
        L1.append(x0)
        L2.append(y)
        i+=1
    return L1,L2

X,Y=fonction(-15,0,1,10,100)
Z=[np.exp(-15*x) for x in X]
print(X,len(X))
print(Y,len(Y))
print(Z,len(Z))
plt.plot(X,Y)
plt.plot(X,Z)
plt.show()