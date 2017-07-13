import math
import numpy as np

# custom imports
from variables import *
from constants import *

# rho function
def rho(r):
    a = (1) / (math.sqrt( 2 * pi ) * sigma )
    b = math.exp( - (phi(r) / sigma ** 2 ) )
    c = a * b
    return c

# phi function
def phi(x):
    if x == 0:
        return -4 * pi * f_0 * G * R_s**2

    a = - ( 4 * pi * G * f_0 * R_s ** 3 ) / x
    b = np.log(1. + (x / R_s) )
    c = a * b
    return c

def phi_3d(x,y,z):
    r = sqrt(x**2 + y**2 + z**2)
    a = - ( 4 * pi * G * f_0 * R_s ** 3 ) / r
    b = np.log(1. + (r / R_s) )
    c = a * b
    return c

def DxDxphi(x, y, z):
    h = 0.01 # pc
    result = phi(x+h, y, z) - 2 * phi(x, y, z) + phi(x-h, y, z)
    result = result / h**2
    return result

def DyDyphi(x, y, z):
    h = 0.01 # pc
    result = phi(x, y+h, z) - 2 * phi(x, y, z) + phi(x, y-h, z)
    result = result / h**2
    return result

def DxDyphi(x, y, z):
    h = 0.01 # pc
    k = 0.01 # pc
    result = phi(x+h, y+k, z) - phi(x+h, y-k, z) - phi(x-h, y+k, z) + phi(x-h, y-k, z)
    result = result / (4*h*k)
    return result
