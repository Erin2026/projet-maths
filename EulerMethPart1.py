import matplotlib.pyplot as plt
import numpy as np



def euler(cst,t0,y0,z,N):
    #initialisation
    tab_t=np.zeros(N)
    tab_y=np.zeros(N)
    pas=z/N
    t=t0
    y=y0

    #méthode d'euler
    for i in range (N):
        tab_t[i]=t
        tab_y[i]=y
        (t,y) = (t+pas,y-(cst*y)*pas)
    return (tab_t,tab_y)

k=2

t0=0
y0=1 #conditions initiales

z=1 #fin de l'intervalle

N=1000 #nombre de points

#graphique pour la solution simple
T,Y=euler(k,t0,y0,z,N)
Z=[np.exp(-k*x) for x in T]
plt.figure("y en fonction de t : solution")

plt.plot(T,Y,'.-',label="solution par la méthode d'euler")
plt.plot(T,Z,label="vraie solution")
plt.xlabel("t")
plt.ylabel("y=f(t)")
plt.legend()
plt.figure("erreur en fonction de t")

#graphique d'erreur 
erreur=abs(Y-Z)
plt.plot(T,erreur,label="erreur")
plt.xlabel("t")
plt.ylabel("erreur")

#graphique pour un k variant de -2 à 2
def lerp (a,b,t):
    return a+(b-a)*t

def colorLerp(t,A,B):
    return (lerp(A[0],B[0],t),lerp(A[1],B[1],t),lerp(A[2],B[2],t))

plt.figure("y en fonction de t avec k non constant")
plt.xlabel("t")
plt.ylabel("y=y(t)")
for i in np.linspace(-2,2,1000):
    T,y=euler(i,t0,y0,z,N)
    plt.plot(T,y,color=colorLerp(((i+2)/4),(121.0/255,27.0/255,171.0/255),(196.0/255,18.0/255,36.0/255)))

#graphique pour 4 y0 différents
plt.figure("y en fonction de t avec 4 valeurs de y0")

y01=2
y02=3
y03=-2
y04=-1

Y1=euler(k,t0,y01,z,N)[1]
Y2=euler(k,t0,y02,z,N)[1]
Y3=euler(k,t0,y03,z,N)[1]
T,Y4=euler(k,t0,y04,z,N)
plt.plot(T,Y1,label="y0=2")
plt.plot(T,Y2,label="y0=3")
plt.plot(T,Y3,label="y0=0")
plt.plot(T,Y4,label="y0=-1")
plt.legend()
plt.xlabel("t")
plt.ylabel("y=y(t)")
plt.show()