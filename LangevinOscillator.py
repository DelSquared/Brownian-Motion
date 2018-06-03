import numpy as np 
from scipy.integrate import odeint
from matplotlib import pyplot as plt

w,g=5,0
#the differential equation z'= i(w+gR(T))z is very sensitive on these parameters k and m.
#The odeint() functon may not work with some values because it thinks that there may not be convergence.
#Do note that there are still some bugs in this code. It is advised to wait for a revised edition before taking a look at it.

def R(t): #R is the "random force" term
  return np.random.normal(0,1) 

def LangevinOscillator (x,t): #Defining the ODE
  z=x[0]+1j*x[1]
  print("z=",z)
  dz=1j*(w+g*R(t))*z
  print("dz=",dz)
  return np.real(dz),np.imag(dz)

t=np.linspace(0,1000,100000)
X=np.array([1,0]) #Initial conditions

x=odeint(LangevinOscillator,X,t)
A=x[:,0]**2 + x[:,1]**2

fig=plt.figure(figsize=((2**13)/100,(2**10)/100))
plt.plot(t,A,label="amplitude")
#plt.plot(t,xv[:,1],label="position")
fig.savefig('soln.png')
