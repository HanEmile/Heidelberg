from numpy import genfromtxt
import numpy as np
import math
import time
import os
import socket
host = socket.gethostname()

from time import gmtime, strftime
mytime = strftime("%H_%M_%S", gmtime())

# controll
star_size = 0.1

# variables
sigma = 200
f_0 = 0.1
R_s = 1e4

# M..
Mxx = 8e-6
Mxy = 0
Myy = -8e-6

# constants
pi = math.pi
e = math.e
G = 4.302e-3

# rho function
def rho(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    a = (1) / (math.sqrt( 2 * pi ) * sigma )
    b = math.exp( - (phi(r) / sigma ** 2 ) )
    c = a * b
    return c

def rho_new(x, y, z):
    a = (1 - ((1) / (2 * (sigma ** 2))) * ( Mxx * x**2 + 2 * Mxy * x * y + Myy * y**2 ) )
    return rho(x, y, z) * a

# phi function
def phi(x):
    if x == 0:
        return -4 * pi * f_0 * G * R_s**2

    a = - ( 4 * pi * G * f_0 * R_s ** 3 ) / x
    b = np.log(1. + (x / R_s) )
    c = a * b
    return c

def gen_stars(stars, print_time=False):
    stars = int(stars)

    time_start = time.time()

    # lists
    listrho = []

    # create new file for every calculation
    path = "data/" + str(host) + "_" + str(os.getpid()) + ".csv"
    print("path: " + str(path))

    length = 1e5

    range_min = -int(length)
    range_max = int(length)

    rand_min = rho_new(0, 0, 0)
    rand_max = rho_new(length, length, length)

    # create random stars
    for r in range(0, stars):
        x = np.random.uniform(range_min, range_max, size=1)
        y = np.random.uniform(range_min, range_max, size=1)
        z = np.random.uniform(range_min, range_max, size=1)
        rand_val = np.random.uniform(rand_min, rand_max, size=1)

        if rand_val < rho_new(x, y, z):
            with open(path, "a") as data:
                data.write(str(x).strip("[]") + "," + str(y).strip("[]") + "," + str(z).strip("[]") + "\n")

    time_all = time.time() - time_start

    if print_time == True:
        print("time: " + str(round(time_all, 2)) + " s")

# generate n stars
gen_stars(1e7, True)

################################################################################

# Benchmarks:
# 1e5 Stars: ~2.93    seconds
# 1e6 Stars: ~29.38   seconds
# 1e7 Stars: ~315.67  seconds
# 1e9 Stars: ~9       hours     (~32400 seconds)

# Knockouts:
# 1e9 Stars: -> ~45000 Stars

# File sizes
# 1 MB ~ 10000 Stars
