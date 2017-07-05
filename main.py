import math # math
import matplotlib.pyplot as plt # plot graphs
import numpy as np # advanced math
import scipy as sp
from scipy.interpolate import InterpolatedUnivariateSpline # use splines
import bpy # controll Blender

# controll
samples = 100
star_size = 0.5
mesh = 'cube' # cube / pyramid

# constants
pi = math.pi
e = math.e
G = 6.67408e-11
Msun = 2e30
pctom = 3e16

# variables
sigma = 200e3
f_0 = 1. * Msun/pctom**3
R_s = 1e4 * pctom

# lists
lista = []
listb = []

# arrays
arr_r = np.logspace(-2, 5, num=samples) * pctom
arr_rho = np.zeros((samples, 1))

# phi function
def phi(x):
    a = - ( 4 * pi * G * f_0 * R_s ** 3 ) / x
    b = np.log(1. + (x / R_s) )
    c = a * b
    return c

# rho function
def rho(r):
    a = (1) # / (math.sqrt( 2 * pi ) * sigma )
    b = math.exp( - (phi(r) / sigma ** 2 ) )
    c = a * b
    return c

# generate arr_rho content
for r in range(samples):
    arr_rho[r] = rho(arr_r[r])

# squeez arrays to 1D
arr_r = np.asarray(arr_r).squeeze()
arr_rho = np.asarray(arr_rho).squeeze()

# interpolation -> spline
x = arr_r
y = arr_rho

spl = InterpolatedUnivariateSpline(x, y)
xs = np.logspace(-4, 5, 1000) * pctom

# plot spline
plt.plot(xs, spl(xs), 'g--', lw=2, alpha=0.7)

# plot rho
plt.plot(arr_r, arr_rho, 'b.')

def create_star(r):
    bpy.ops.mesh.primitive_cone_add(vertices=3, radius1=star_size, radius2=0, depth=star_size, location=(r, 0, 0) )
    bpy.ops.mesh.primitive_cube_add(radius=star_size, location=(r, 0, 0) )

for r in range(0, 1000):
    rand_val = np.random.uniform(0, 5e60, size=1)
    lista.append(rand_val)
    print("{:<5}{:<20}{:<20}".format(str(r), str(spl(xs)[r]), str(rand_val) ), end="")

    if rand_val < spl(xs)[r]:
        print("☆")
        create_star(r)
    else:
        print("")

# plot random value
plt.plot(rand_val)

# plot settings
plt.title("Rho")
plt.legend(['interpolation', 'rho', 'rand'])
plt.xscale('log')
plt.autoscale()

# display plot
plt.show()
