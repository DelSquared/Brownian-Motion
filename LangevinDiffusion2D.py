import numpy as np 
from matplotlib import pyplot as plt

def ODE (xo,t,noisemap): #example ODE
  N=noisemap
  x,v=xo
  return np.array([v,20*N-v])

def integrator3(f,xo,t,N): #Order 3
  x=np.zeros(shape=(xo.shape[0],t.shape[0]), dtype=complex)
  x[:,0]=xo
  dt=t[1]-t[0]
  for i in range(t.shape[0]-1):
    k1=f(x[:,i],t[i], N[i])
    k2=f(x[:,i]+k1*dt/2, t[i]+dt/2, N[i])
    x[:,i+1]=x[:,i]+f( x[:,i]+k2*dt/2 , t[i]+dt/2 ,N[i])*dt
  return x

t=np.linspace(0,50,5000)
N=np.random.normal(0,1,size=(2,t.shape[0]))
xo=np.array([0+0j,5+0j])
yo=np.array([0+0j,5+0j])
print("doing x")
x=integrator3(ODE,xo,t,N[0,:])
print("doing y")
y=integrator3(ODE,yo,t,N[1,:])
xy=np.append(x,y,axis=0)

print("plotting")
print(xy.shape)


def animate(state, t):

    # Plot initial plot so that we can change underlying data later
    plt.plot(np.real(state[0,0]),np.real(state[2,0]), 'r.',markersize=15)

    # Set limits of plot
    plt.xlim([-1, 10])
    plt.ylim([-1, 10])
    # Animate the position of the pendulum in time
    for i in range(1, state.shape[1] - 1):
        plt.plot(np.real(state[0,i-1]),np.real(state[2,i-1]), 'w.',markersize=20)
        plt.plot(np.real(state[0,i]),np.real(state[2,i]), 'r.',markersize=15)

        plt.draw()
        plt.pause(0.05)

plt.figure(figsize=(12, 6))
animate(xy,t)
