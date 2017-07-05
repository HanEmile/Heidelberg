# Import
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

# controll
draw = False
samples = 100

# Variables
sigma = 200
f_0 = 10 # M_O / pc^3
R_s = 100 # kpc

# constants
e = math.e
pi = math.pi
G = 6.67330 * math.pow(10, -11)
parsec_m = 3.0857 * math.pow(10, 16) # 1 parsec in meter
sunmass = 1.988435 * math.pow(10, 30) # kg

# parsec to meter converter method
def parsec2meter(value):
    return value * parsec_m

# lists
lista = []
listb = []

# phi function
def phi(r):
    a = - ( 4 * pi * G * f_0 * math.pow(R_s, 3) ) / r
    b = np.log( 1 + r / R_s )
    return a * b

# rho function
def rho(r):
    a = (1) / (math.sqrt( 2 * pi ) * sigma )
    b = math.pow(e, - (phi(r) / math.pow(sigma, 2) ) )
    listb.append(a * b)
    return a * b

# Numpy
arr_r = np.zeros((samples, 1))
arr_rho = np.zeros((samples, 1))

# generate arr_r
arr_r = np.logspace(0, 10, 100)
# print(arr_r)

# generate arr_rho
for r in range(samples):
    arr_rho[r] = rho(arr_r[r])

    lista.append(arr_rho[r])
    # print("{:<3}{:<15}{:<15}".format(str(r), str(arr_r[r]), str(arr_rho[r])))

# print(arr_r)
print(arr_rho)

# form array -> 1D
arr_r = np.asarray(arr_r)
arr_r = np.asarray(arr_r).squeeze()
arr_rho = np.asarray(arr_rho).squeeze()

# define axis
x = arr_r
y = arr_rho

# generate spline
xs = np.logspace(0, 100, 10000)
# spl = UnivariateSpline(x, y)
spl = InterpolatedUnivariateSpline(x, y, k = 3)
spl.set_smoothing_factor(0.00001)

# get value from spline
# def spline_val(pos):
#     return spl.__call__(1, nu=0, ext=None)

# for x in range(1, 2, 0.1):
    # print(spline_val(x))

# Plot firts term of rho
# plt.plot(listb)

# Plot raw_data
# plt.plot(x, y, 'ro', ms=5)

# Plot spline
# plt.plot(xs, spl(xs), 'b-', ms=5)

# Plot Settings
# plt.xscale('log')
# plt.title('InterpolatedUnivariateSpline')
# plt.legend(['raw values', 'spline'])
# plt.xlim(0.6, 100)
# plt.ylim(-0.1, 1)
plt.show()
