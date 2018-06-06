import numpy as np 
from matplotlib import pyplot as plt
#The intention of this solver is to eliminate the use of Scipy's odeint from this project. While it is a phenomenal tool
#its design makes it less than ideal for dealing with noisy/stochastic ODEs. 

k=5 #Set to 0 to disable noise for example

def ODE (x,t,noisemap): #example ODE
  N=noisemap
  return 1j*(1+k*N)*x

def integrator1(f,xo,t,N): #Order 1 (Euler's method)
  x=np.zeros_like(t, dtype=complex)
  x[0]=xo
  dt=t[1]-t[0]
  for i in range(t.shape[0]-1):
    x[i+1]=x[i]+f(x[i],t[i],N[i])*dt
  return x

def integrator2(f,xo,t,N): #Order 2 (Modified Euler/Midpoint method)
  x=np.zeros_like(t, dtype=complex)
  x[0]=xo
  dt=t[1]-t[0]
  for i in range(t.shape[0]-1):
    k1=f(x[i], t[i], N[i])
    x[i+1]=x[i]+f(x[i]+k1*dt/2, t[i]+dt/2, N[i])*dt
  return x

def integrator3(f,xo,t,N): #Order 3
  x=np.zeros_like(t, dtype=complex)
  x[0]=xo
  dt=t[1]-t[0]
  for i in range(t.shape[0]-1):
    k1=f(x[i],t[i], N[i])
    k2=f(x[i]+k1*dt/2, t[i]+dt/2, N[i])
    x[i+1]=x[i]+f( x[i]+k2*dt/2 , t[i]+dt/2 ,N[i])*dt
  return x

def integrator4(f,xo,t,N): #Order 4 (still requires a more exhaustive testing to be carried out)
  x=np.zeros_like(t, dtype=complex)
  x[0]=xo
  dt=t[1]-t[0]
  for i in range(t.shape[0]-1):
    k1=f(x[i],t[i],N[i])
    k2=f(x[i]+k1*dt/2, t[i]+dt/2, N[i])
    k3=f(x[i]+k2*dt/2, t[i]+dt/2, N[i])
    x[i+1]=x[i]+f(x[i]+k3*dt/2, t[i]+dt/2, N[i])*dt
  return x

def integrator5(f,xo,t,N): #Order 5 (still requires a more exhaustive testing to be carried out)
  x=np.zeros_like(t, dtype=complex)
  x[0]=xo
  dt=t[1]-t[0]
  for i in range(t.shape[0]-1):
    k1=f(x[i],t[i],N[i])
    k2=f(x[i]+k1*dt/2, t[i]+dt/2, N[i])
    k3=f(x[i]+k2*dt/2, t[i]+dt/2, N[i])
    k4=f(x[i]+k3*dt/2, t[i]+dt/2, N[i])
    x[i+1]=x[i]+f(x[i]+k4*dt/2, t[i]+dt/2, N[i])*dt
  return x

t=np.linspace(0,50,5000)
N=np.random.normal(0,1,size=(t.shape[0]))

x1=integrator1(ODE,5+1j,t,N) #Trying all solvers for comparison
x2=integrator2(ODE,5+1j,t,N)
x3=integrator3(ODE,5+1j,t,N)
x4=integrator4(ODE,5+1j,t,N)
x5=integrator5(ODE,5+1j,t,N)

fig=plt.figure(figsize=((2**13)/100,(2**10)/100)) #Plotting
plt.plot(t,np.real(x1),label="real amplitude(1)")
plt.plot(t,np.real(x2),label="real amplitude(2)")
plt.plot(t,np.real(x3),label="real amplitude(3)")
plt.plot(t,np.real(x4),label="real amplitude(4)")
plt.plot(t,np.real(x5),label="real amplitude(5)")
plt.ylim(-10,10)
fig.savefig('soln.png')
