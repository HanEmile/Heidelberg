import math # math
import matplotlib.pyplot as plt # plot graphs
import numpy as np # advanced math
import scipy as sp
from scipy.interpolate import InterpolatedUnivariateSpline # use splines
# import bpy # controll Blender

# controll
samples = 100

# constants
pi = math.pi
e = math.e
G = 6.67408 * math.pow(10, -11)

# variables
sigma = 200
f_0 = 10
R_s = 10

# lists
lista = []
listb = []

# arrays
arr_r = np.logspace(-2, 3, num=samples)
arr_rho = np.zeros((samples, 1))

# phi function
def phi(x):
    a = - ( 4 * pi * G * f_0 * math.pow(R_s, 3) ) / x
    b = math.log(e, 1 + (x / R_s) )
    c = a * b
    return c

# rho function
def rho(r):
    a = (1) / (math.sqrt( 2 * pi ) * sigma )
    b = math.pow(e, - (phi(r) / math.pow(sigma, 2) ) )
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
xs = np.logspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'g--', lw=2, alpha=0.7)

# print(spl(xs)[1])

for x in range(0, 1000):
    spl(xs)[x]

# for value in range(len(spl(xs))):
    # print("{:<30}{:<30}".format(xs[value], spl(xs)[value] ) )


# plot rho
plt.plot(arr_r, arr_rho, 'b.')

# plot settings
plt.title("Rho")
plt.legend(['interpolation', 'rho'])
plt.xscale('log')
plt.autoscale()

# display plot
plt.show()
