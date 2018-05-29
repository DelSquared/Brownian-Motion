import numpy as np 
from scipy.integrate import odeint
from matplotlib import pyplot as plt

k,m=0.000001,1.5 
#the differential equation y''= -my + kR is very sensitive on these parameters k and m.
#The odeint() functon may not work with some values because it thinks that there may not be convergence.

def R(t): #R is the "random force" term
  return np.random.normal(0,1) 

def Langevin (xv,t): #Defining the ODE
  x,v=xv
  dxv=[v,-m*v+k*R(t)]
  return dxv

t=np.linspace(0,1000,1000000)
XV=np.array([0,1]) #Initial conditions

xv=odeint(Langevin,XV,t)

fig=plt.figure(figsize=((2**13)/100,(2**10)/100))
plt.plot(t,xv[:,0],label="velocity")
plt.plot(t,xv[:,1],label="position")
fig.savefig('soln.png')
