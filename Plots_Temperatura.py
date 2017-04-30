
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.io.wavfile
from scipy.fftpack import fft, fftfreq, ifft
get_ipython().magic('matplotlib inline')


# In[14]:

#Debo aclarar que inicialmente hice el programa en python pero solo lo pasé parcialmente a #lenguaje c
#Ya que los procesos de python son muy lentos para grandes iteraciones, solo lo hice para t=0 y #t=100, para t=2500 la lógica es exactamente la misma.
#Se declaran algunas constantes
n_x=100
n_y=100
n_t=2500


nu = 10**-4
sigma = 0.3
x=np.linspace(0,100,n_x)
y=np.linspace(0,100,n_y)
dx=x[1]-x[0]
dy=x[1]-x[0]

dt=sigma*dx**2/nu
alpha=dt/dx**2

#creo matriz lennas de 50
u=50*np.ones([n_x,n_y])
#lleno el rango especificado con temperatura 100
for i in range(15,30):
    for j in range(40,60):
        u[i,j]=100
        
#creé copias de las listas para no tener problemas cada que se hacen nuevos cálculos
uf=(u)
up=(u)
ua=(u)
uf2=(u)
up2=(u)
ua2=(u)

uf100=(u)
up100=(u)
ua100=(u)
uf2100=(u)
up2100=(u)
ua2100=(u)

#habiendo solucionado la ecuación para uf, recorro el array sin los extremos del mismo, para #garantizar que estos sean fijos
for n in range(0,0):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            uf[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
    

fig = plt.figure()
x, y = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, uf, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionFijaInic')


# In[7]:


#para la periódica, recorro el array de la misma forma, pero a diferencia de la anterior, debo #considerar que:
#la primera columna del array(fija) sea igual a la penúltima, que está sometida a modificaciones. #También, que la última columna
#(fija)sea igual a la segunda(modificable). De manera analoga pensamos el problema para las filas. 
#De esta manera aseguro una periodicidad en los extremos como se ve en la gráfica
for n in range(0,0):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            
       
            up[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
            
            up[0,:]=up[n_x-2,:]
            up[n_y-1,:]=up[1,:]
            
            up[:,0]=up[:,n_x-2]
            up[:,n_y-1]=up[:,1]
            

fig2 = plt.figure()
x2, y2 = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, up, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionPeriodicaInic')


# In[8]:

#Para el caso de condiciones abiertas, debo asegurar que:
#la primera columna de mi array, que es fija, sea igual a la segunda(variable), de la misma forma #la última que es fija, debe 
#ser igual a la penúltima, la cuál está sometida a modeficaciones. Así, la temperatura tiene #cierta libertad, condiciones abiertas.
#En la gráfica vemos como la temperatura tiende a escaparse por el lado donde más cerca estaba.
for n in range(0,0):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            
       
            ua[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
            
            ua[0,:]=ua[1,:]
            ua[n_x-1,:]=ua[n_x-2,:]
            
            ua[:,n_x-1]=ua[:,n_x-2]
            ua[:,0]=ua[:,1]

fig3 = plt.figure()
x3, y3 = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, ua, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionAbiertaInic')


# In[9]:

#Para las siguientes 3 gráficas(caso dos), pensamos el problema de la misma forma, pero esta vez, #aseguramos que haya un espacio
#(el establecido por la tarea), donde la temperatura sea constante a 100 grados.
for n in range(0,0):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            uf2[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
            uf2[20:40,45:55] = 100
fig4 = plt.figure()
x4, y4 = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, uf2, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionFijaInic2')


# In[11]:

for n in range(0,0):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            
       
            up2[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
            
            up2[0,:]=up2[n_x-2,:]
            up2[n_y-1,:]=up2[1,:]
            
            up2[:,0]=up2[:,n_x-2]
            up2[:,n_y-1]=up2[:,1]
            
            up2[20:40,45:55] = 100
            

fig5 = plt.figure()
x5, y5 = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, up2, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionPeriodicaInic2')


# In[12]:

for n in range(0,0):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            
       
            ua2[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
            
            ua2[0,:]=ua2[1,:]
            ua2[n_x-1,:]=ua2[n_x-2,:]
            
            ua2[:,n_x-1]=ua2[:,n_x-2]
            ua2[:,0]=ua2[:,1]
            
            ua2[20:40,45:55] = 100

fig6 = plt.figure()
x6, y6 = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, ua2, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionAbiertaInic2')


# In[15]:

for n in range(0,100):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            uf100[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
    

fig7 = plt.figure()
x7, y7 = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, uf100, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionFija100')


# In[16]:

for n in range(0,100):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            
       
            up100[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
            
            up100[0,:]=up100[n_x-2,:]
            up100[n_y-1,:]=up100[1,:]
            
            up100[:,0]=up100[:,n_x-2]
            up100[:,n_y-1]=up100[:,1]
            

fig8 = plt.figure()
x8, y8 = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, up100, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionPeriodica100')


# In[17]:

for n in range(0,100):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            
       
            ua100[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
            
            ua100[0,:]=ua100[1,:]
            ua100[n_x-1,:]=ua100[n_x-2,:]
            
            ua100[:,n_x-1]=ua100[:,n_x-2]
            ua100[:,0]=ua100[:,1]

fig9 = plt.figure()
x9, y9 = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, ua100, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionAbierta100')


# In[18]:

for n in range(0,100):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            uf2100[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
            uf2100[20:40,45:55] = 100
fig10 = plt.figure()
x10, y10 = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, uf2100, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionFija1002')


# In[19]:

for n in range(0,100):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            
       
            up2100[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
            
            up2100[0,:]=up2100[n_x-2,:]
            up2100[n_y-1,:]=up2100[1,:]
            
            up2100[:,0]=up2100[:,n_x-2]
            up2100[:,n_y-1]=up2100[:,1]
            
            up2100[20:40,45:55] = 100
            

fig11 = plt.figure()
x11, y11 = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, up2100, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionPeriodica1002')


# In[20]:

for n in range(0,100):
    u_past=u.copy()
    for i in range(1,n_x-1):
        for j in range(1,n_y-1):
            
       
            ua2100[i][j]=u_past[i,j]*(1-4*nu*alpha)  +  u_past[i+1,j]*alpha*nu  +  u_past[i-1,j]*nu*alpha  +  u_past[i,j+1]*nu*alpha  +  u[i,j-1]*nu*alpha  
            
            ua2100[0,:]=ua2100[1,:]
            ua2100[n_x-1,:]=ua2100[n_x-2,:]
            
            ua2100[:,n_x-1]=ua2100[:,n_x-2]
            ua2100[:,0]=ua2100[:,1]
            
            ua2100[20:40,45:55] = 100

fig12 = plt.figure()
x12, y12 = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, ua2100, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=1)
plt.savefig('DifusionAbierta1002')


# In[ ]:



