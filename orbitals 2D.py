#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm
from scipy.special import assoc_laguerre


#### set the quantum numbers
n = float(input("Enter n: Note that n should > 0 \n"))
l = float(input("Enter l: Note that l should in [0,n-1] \n"))
m = float(input("Enter m: Note that m should in [-l,l] \n"))

x = np.linspace(-n**2*4, n**2*4, 500)
y = 0  #### the plane locates at y = 0 
z = np.linspace(-n**2*4, n**2*4, 500)
X, Z = np.meshgrid(x, z)

rho = np.linalg.norm((X,y,Z), axis=0) / n
Lag = assoc_laguerre(2 * rho, n - l - 1, 2 * l + 1)
Ylm  = sph_harm(m, l, np.arctan2(y,X), np.arctan2(np.linalg.norm((X,y), axis=0), Z))
Psi = np.exp(-rho) * np.power((2*rho),l) * Lag * Ylm

density = np.conjugate(Psi) * Psi
density = density.real

#### visualization
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(density.real, extent=[-density.max()*0.1,density.max()*0.1,  
                                -density.max()*0.1,density.max()*0.1])
plt.show()
## fig.savefig("H_psi420.png", dpi=300)