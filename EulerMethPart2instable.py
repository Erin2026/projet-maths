import matplotlib.pyplot as plt
import numpy as np


def euler(x0,v0,z,N):
    #initialisation
    tab_x = np.zeros(N)
    tab_v = np.zeros(N)
    tab_t = np.zeros(N)
    pas=z/N
    c=g/l
    x=x0
    v=v0
    t=0

    #méthode d'euler
    for i in range (N):
        tab_t[i]=t
        tab_x[i]=x
        tab_v[i]=v
        (t,x,v)= (t+pas,x+v*pas,v-c*np.sin(x)*pas)
    return (tab_t,tab_x,tab_v)

g=10
l=2
N=1000
x0=1
v0=1
z=10

(t,x,v)=euler(x0,v0,z,N)

#graphique de la sotution de la méthode d'euler explicite
plt.figure("position angulaire (theta) en fonction de t")
plt.plot(t,x)
plt.xlabel("t")
plt.ylabel("theta(t)")
plt.grid()

#graphique de la vitesse en fonction de la position, instable
plt.figure ("vitesse angulaire (theta point) en fonction de la position angulaire (theta)")
plt.plot(x,v)
plt.xlabel("theta")
plt.ylabel("theta point")
plt.show()