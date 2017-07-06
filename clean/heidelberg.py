import math
import numpy as np

# custom imports
from variables import *
from constants import *

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
