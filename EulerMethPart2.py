import matplotlib.pyplot as plt
import numpy as np


def euler(x0,v0,h,N):
    tab_x = np.zeros(N)
    tab_v = np.zeros(N)
    tab_t = np.arange(N)*h
    c=g/l
    x=x0
    v=v0
    for i in range (N):
        tab_x[i]=x
        tab_v[i]=v
        x=x+v*h
        v=v-c*np.sin(x)*h
    return (tab_t,tab_x,tab_v)
g=10
l=2
h=0.11
N=100
x0=1
v0=1
(t,x,v)=euler(x0,v0,h,N)

plt.figure()
plt.plot(t,x)
plt.xlabel("x")
plt.ylabel("y")
plt.axis()
plt.grid()
plt.show()