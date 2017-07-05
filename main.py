import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.interpolate import InterpolatedUnivariateSpline

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
arr_r = np.logspace(0, 10, num=samples)
arr_r = arr_r - 0.9
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

# interpolation
x = arr_r
y = arr_rho

spl = InterpolatedUnivariateSpline(x, y)
xs = np.linspace(0, 1000, 1000000)
plt.plot(xs, spl(xs), 'g--', lw=3, alpha=0.7)

# plot rho
plt.plot(arr_r, arr_rho, 'b.')

# plot settings
plt.title("Rho")
plt.legend(['interpolation', 'rho'])
plt.xscale('log')
plt.autoscale()

# display plot
plt.show()
