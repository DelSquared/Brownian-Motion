import numpy as np 
from matplotlib import pyplot as plt
#The intention of this solver is to eliminate the use of Scipy's odeint from this project. While it is a phenomenal tool
#its design makes it less than ideal for dealing with noisy/stochastic ODEs. 

#One thing that I fear may have been done inappropriately in this was the implementation of the noise term since it was
#being randomly generated more than once for the same spot (eg. in the second order, the estimate for the midpoint 
#generates a different random number from the calculation of the actual value of that point). One could probably 
#deal with this by running a noise map in order to reference the noise values as needed.

k=1 #Set to 0 to disable noise for example

def ODE (x,t): #example ODE
  return 1j*(1+k*np.random.normal(0,1))*x

def integrator1(f,xo,t): #Order 1 (Euler's method)
  x=np.zeros_like(t, dtype=complex)
  x[0]=xo
  dt=t[1]-t[0]
  for i in range(t.shape[0]-1):
    x[i+1]=x[i]+f(x[i],t)*dt
  return x

def integrator2(f,xo,t): #Order 2 (Modified Euler/Midpoint method)
  x=np.zeros_like(t, dtype=complex)
  x[0]=xo
  dt=t[1]-t[0]
  for i in range(t.shape[0]-1):
    x[i+1]=x[i]+f(x[i]+f(x[i],t)*dt/2,t+dt/2)*dt
  return x

def integrator3(f,xo,t): #Order 3
  x=np.zeros_like(t, dtype=complex)
  x[0]=xo
  dt=t[1]-t[0]
  for i in range(t.shape[0]-1):
    x[i+1]=x[i]+f( x[i]+f( x[i]+f(x[i],t)*dt/2 , t+dt/2 )*dt*dt/2 , t+dt/2 )*dt
  return x

def integrator4(f,xo,t): #Order 4 (still requires a more exhaustive testing to be carried out)
  x=np.zeros_like(t, dtype=complex)
  x[0]=xo
  dt=t[1]-t[0]
  for i in range(t.shape[0]-1):
    x[i+1]=x[i]+f( x[i]+f( x[i]+f( x[i]+f( x[i]+f(x[i],t)*dt/2 , t+dt/2 )*dt*dt/2 , t+dt/2 )*dt/2 , t+dt/2 )*dt*dt/2 , t+dt/2 )*dt
  return x

t=np.linspace(0,100,100000)

x1=integrator1(ODE,5+1j,t) #Trying all solvers for comparison
x2=integrator2(ODE,5+1j,t)
x3=integrator3(ODE,5+1j,t)
x4=integrator4(ODE,5+1j,t)

fig=plt.figure(figsize=((2**13)/100,(2**10)/100)) #Plotting
plt.plot(t,np.real(x1),label="real amplitude(1)")
plt.plot(t,np.real(x2),label="real amplitude(2)")
plt.plot(t,np.real(x3),label="real amplitude(3)")
plt.plot(t,np.real(x4),label="real amplitude(4)")
fig.savefig('soln.png')
