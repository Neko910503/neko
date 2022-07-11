import numpy as np
from scipy.special import sph_harm 
import matplotlib.pyplot as plt
from matplotlib import cm 
from mpl_toolkits.mplot3d import Axes3D


l = float(input("Enter l value: Note that l should >= 0 \n"))
m = float(input("Enter m value: Note that m should in [-l, l] \n"))

'''
set angles (theta and phi). 
Note: in Scipy, theta and phi are azimuthal angle and polar angle, respectively.
'''
theta = np.linspace(0, 2 * np.pi, 181)
phi   = np.linspace(0, np.pi, 91)
theta_2d, phi_2d = np.meshgrid(theta, phi)

Ylm = sph_harm(abs(m), l, theta_2d, phi_2d)

xyz_2d = np.array([np.sin(phi_2d) * np.sin(theta_2d),
                   np.sin(phi_2d) * np.cos(theta_2d),
                   np.cos(phi_2d)]) 

#### Linear combination of Y_{l,m} and Y_{l,-m} to create the real form.
#### see https://en.wikipedia.org/wiki/Spherical_harmonics#Real_form
if m < 0:
    Ylm = np.sqrt(2) * (-1)**m * Ylm.imag
elif m > 0:
    Ylm = np.sqrt(2) * (-1)**m * Ylm.real
r = np.abs(Ylm.real) * xyz_2d


#### visualization
colormap = cm.ScalarMappable(cmap=plt.get_cmap("RdYlBu_r"))
colormap.set_clim(-0.5, 0.5)
limit = 0.5

fig = plt.figure(figsize=plt.figaspect(1.))
ax = fig.add_subplot(111, projection='3d')
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([0.75, 0.75, 1, 1]))
ax.plot_surface(r[0], r[1], r[2],
                facecolors=colormap.to_rgba(Ylm.real),
                rstride=1, cstride=1)
ax.set_xlim(-limit,limit)
ax.set_ylim(-limit,limit)
ax.set_zlim(-limit,limit)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()