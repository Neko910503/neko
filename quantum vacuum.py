import numpy as np
from scipy.constants import hbar, c
import matplotlib.pyplot as plt

L = 1e-6 # size of the simulation box (m)
N = 100 # number of grid points
dx = L/N # grid spacing
dt = dx/(2*c) # time step
T = 1e-15 # total simulation time (s)

psi = np.zeros((N,N), dtype=complex) # initialize wave function
psi[N//2,N//2] = 1 # set initial state to vacuum state

for n in range(int(T/dt)):
    psi = np.fft.ifft2(np.exp(-1j*hbar*dt*np.fft.fftn(np.abs(psi)**2)))
    
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, y)
Z = np.abs(psi)**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('Probability Density')
plt.show()