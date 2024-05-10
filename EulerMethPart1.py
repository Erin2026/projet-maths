import matplotlib.pyplot as plt
import numpy as np
print("pour une équation différentielle de la forme y'=ay, x représente l'abscisse de la condition initiale, y son ordonnée, z la fin de l'intervalle et h le nombre de points attendus")

def fonction(a,x,y,z,h):
    L1=[x]
    L2=[y]
    i=x
    pas=(z-i)/h
    while i<h:
        x=x+pas
        y=y+(a*y)*pas
        L1.append(x)
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