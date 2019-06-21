# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:23:22 2019

@author: David
"""
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
import numpy as np


x = np.linspace(1,3,3)
y = np.linspace(1,3,3)
xy = np.dstack(np.meshgrid(x, y)).reshape(-1, 2)
z = xy[:,1].shape
#print(z[0] )
#print()
u = lambda x,y : np.exp(x*y)
#print()
#print(len(xy.shape))

#for i in range(xy[:,1].shape[0]):
#    print(xy[i])
   


        
class function3D:  
   def __init__(self,xy,funct):
       self.xy=xy
       self.u=funct
       self.x=np.linspace(-360,360)
        
   def calculate(self,i):
#       for i in range(xy[:,0].shape[0]):
      
        result = [self.u(self.x[j],i) for j in range(len(self.x)) ]
        self.res=result
        return result
    
    
   def get_size_frame(self):
        print(len(self.x))
        v1 = len(self.x)
       
        return int(v1)
        
        
   def update_HTML_animation(self, i, arg):
       ax = plt.gca()

       arg.clf()
       res= self.calculate(i)
       plt.plot(self.x,self.res)
       #.plt.scatter(-360,360)
              
       
            # z = plt.plot(self.r[:, 0], self.r[:, 1], color='blue')
            #plt.draw()
       ax.spines['left'].set_position('zero')
       ax.spines['right'].set_color('none')
       ax.spines['top'].set_color('none')
    
       return self.x


u = lambda x,y : np.sin(np.pi*(x/360 ) - np.pi*(100*y/360 ))
#z = lambda x,y : y*np.sin(np.pi*( x/360 ))
#a = np.linspace(-360,360)
#result = [u(a[j],100) for j in range(len(a)) ]
#plt.plot(a,result)
#plt.show()

f = function3D(None,u)



# print(size)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
fig = plt.figure(figsize=(6, 6))
fig = plt.figure(figsize=(6, 6))
size = f.get_size_frame()
size2 = 54.

#
#for i in range(size):
#    res= f.calculate(i)
#    plt.plot(f.x,f.res)
#    plt.show()
    
    
anim = animation.FuncAnimation(plt.gcf(), f.update_HTML_animation, interval=10000000000, fargs=(fig,), frames=size, blit=False)
anim.save('wave9.mp4', writer=writer)
#HTML(anim.to_html5_video())




        