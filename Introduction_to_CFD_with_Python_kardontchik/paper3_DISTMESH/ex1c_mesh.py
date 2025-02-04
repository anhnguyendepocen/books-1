"""
   Usage: run ex1c_mesh
   Uniform mesh on a circle
"""
import numpy as np
from numpy import pi as pi
from scipy.spatial import Delaunay
import matplotlib.pylab as plt

from DISTMESH import *

# -------------------- Optional plot ---------------------------------------

def plot_shapes(xc,yc,r):
    # circle for plotting
    t_cir = np.linspace(0,2*pi)
    x_cir = xc + r*np.cos(t_cir)
    y_cir = yc + r*np.sin(t_cir)

    plt.figure()
    plt.plot(x_cir,y_cir)
    plt.grid()
    plt.title('Shapes')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.show()
    return

# ------------- Optional plot ---------------------------------------

plt.close('all')

# Circle parameters:
# center at (xc,yc), radius r
xc = 0; yc = 0; r = 1.0
# Rectangle vertices:
x1,y1 = -1.0,-2.0
x2,y2 = 2.0,3.0

plot_shapes(xc,yc,r)

# Define the region in (x,y) plane in which we will create the mesh
# and the grid granularity
xmin = -1.5; ymin = -1.5
xmax = 1.5; ymax = 1.5
h0 = 0.1 

# any fixed [xp,yp] points on the boundary?
pfix = np.zeros((0,2))   # null 2D array, no fixed points provided

# distance functions
fd = Circle(xc,yc,r)

# size function
fh = lambda p: np.ones(len(p))

p,t,bars = distmesh(fd,fh,h0,xmin,ymin,xmax,ymax,pfix,Iflag=4)
tri,bbars = find_boundary(p,t,fh)

boundary_nodes,boundary = boundary_info(p,bbars)
