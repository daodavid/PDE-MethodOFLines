# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:56:38 2019

@author: David
"""
# https://www.youtube.com/watch?v=6-2Wzs0sXd8
#for j in range(1,len(t)):
#    plt.clf()
#    for i in range(1,n-1):
#        z = -(T[i]-T[i-1])/dx**2
#        z1 = (T[i+1]-T[i])/dx**2
#        dTdt[i] = alpha*(z+z1)
#    p1 = (-T[0]-T1s)/dx**2
#    p2 = (T[1]-T[0])/dx**2
#    dTdt[0] = alpha*(p1+p2)
#    dTdt[n-1] = alpha*(-(T[n-1]-T[n-2])/dx**2 + (T2s-T[n-1])/dx**2)
#    T=T+dTdt*dt
#    #T=dTdt
#    plt.figure(i)
#    plt.plot(x,T)
#    plt.axis([0,L,0,50])
#    plt.xlabel("Distance (m)")
#    plt.ylabel("Temperture (C)")
#    plt.show()
#    plt.pause(0.01)
    
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML


def update_HTML_animation(j,arg,T,T2s):
        ax = plt.gca()
        L = 0.1
        n=10
        T0 = 0
        T1s = 40
        T2s =20
        dx = L/n
        alpha = 0.00001
        t_final = 60
        dt=0.1

        #q =ax.quiver(0, 0, self.r[i,2],  self.r[i,3], pivot='mid', color='r', units='inches')
        #q = ax.quiver(0, 0, self.r[i, 2], self.r[i, 3], pivot='mid', color='r', units='inches')
       

        arg.clf()
        
        ax.patch.set_facecolor('black')
        particles, = ax.plot([], [], 'bo', ms=6)
      
    
        plt.clf()
        for i in range(1,n-1):
            z = -(T[i]-T[i-1])/dx**2
            z1 = (T[i+1]-T[i])/dx**2
            dTdt[i] = alpha*(z+z1)
        p1 = (-T[0]-T1s)/dx**2
        p2 = (T[1]-T[0])/dx**2
        dTdt[0] = alpha*(p1+p2)
        dTdt[n-1] = alpha*(-(T[n-1]-T[n-2])/dx**2 + (T2s-T[n-1])/dx**2)
        T=T+dTdt*dt
        #T=dTdt
        plt.figure(i)
        plt.plot(x,T)
        plt.draw()
        plt.axis([0,L,0,50])
        plt.xlabel("Distance (m)")
        plt.ylabel("Temperture (C)")
         
        return particles 
L = 0.1
n=10
T0 = 0
T1s = 40
T2s =20
dx = L/n
alpha = 0.00001
t_final = 60
dt=0.1

x = np.linspace(dx/2,L-dx/2,n)
#print(x)

T = np.ones(n)*T0
print(T)
dTdt = np.empty(n)
print(dTdt)

t = np.arange(0,t_final,dt)
print(t)
fig = plt.figure(figsize=(6, 6))
fig = plt.figure(figsize=(6, 6))
    
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

anim = animation.FuncAnimation(plt.gcf(), update_HTML_animation, interval=1,fargs=(fig,T,T2s), frames=100, blit=False)
anim.save('pde-Heat.mp4', writer=writer)
HTML(anim.to_html5_video())    