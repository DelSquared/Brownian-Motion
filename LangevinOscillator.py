import numpy as np 
from scipy.integrate import odeint
from matplotlib import pyplot as plt

w,g=1,1
#the differential equation y''= -my + kR is very sensitive on these parameters k and m.
#The odeint() functon may not work with some values because it thinks that there may not be convergence.

def R(t): #R is the "random force" term
  k=np.random.normal(0,1) 
  #if abs(k)>1.5:
    #k=1.5*k/abs(k)
  return k

def LangevinOscillator (x,t): #Defining the ODE
  z=x[0]+1j*x[1]
  print("z=",z)
  dz=1j*(w+g*R(t))*z
  print("dz=",dz)
  return np.real(dz)*100/10000,np.imag(dz)*100/10000

t=np.linspace(0,100,10000)

x=np.zeros((2,t.shape[0]))
print(x.shape)
print(x[:,0])
x[:,0]=[10,0]
print(x[:,0])
for i in range(10000-1):
  print(i)
  L=LangevinOscillator(x[:,i],0)
  x[:,i+1]=x[:,i]+L

print(x.shape)
fig=plt.figure(figsize=((2**13)/100,(2**10)/100))
plt.plot(t,x[0,:],label="real")
plt.plot(t,x[1,:],label="im")
fig.savefig('soln.png')
