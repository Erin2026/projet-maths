import matplotlib.pyplot as plt
import numpy as np


def euler(t0,x0,v0,z,N,l):
    #initialisation
    tab_x = np.zeros(N)
    tab_v = np.zeros(N)
    tab_t = np.linspace(t0,z,N)
    pas=z/N
    c=g/l
    x=x0
    v=v0

    #méthode d'euler "asymétrique"
    for i in range (N):
        tab_x[i]=x
        tab_v[i]=v
        x=x+v*pas
        v=v-c*np.sin(x)*pas
    return (tab_t,tab_x,tab_v)

g=10
l=2
z=10
N=1000

t0=0
x0=1
v0=1

(t,x,v)=euler(t0,x0,v0,z,N,l)

#graphique de la vraie solution avec la méthode d'euler a symétrique
plt.figure("position angulaire (theta) en fonction de t")
plt.plot(t,x,label="solution par la méthode d'euler")
plt.xlabel("t")
plt.ylabel("theta(t)")
plt.axis()
plt.grid()

#graphique pour 4 l différents
L=[1,2,3,4]
plt.figure("theta en fonction de t, 4 l différents")
for l in L:
    (t,x,v)=euler(t0,x0,v0,z,N,l)
    plt.plot(t,x,label='l='+str(l))
plt.legend()

#graphique pour 4 v (thetha point) différents 
plt.figure("theta en fonction de t, 4 thetap_0 différents")
l=2
T=[-1,1,2,3]
for k in T:
    (t,x,v)=euler(t0,x0,k,z,N,l)
    plt.plot(t,x,label='thetap_0='+str(k))
plt.legend()

plt.show()