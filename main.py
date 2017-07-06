import math # math
import matplotlib.pyplot as plt # plot graphs
import numpy as np # advanced math
import scipy as sp
from scipy.interpolate import InterpolatedUnivariateSpline # use splines
# import bpy # controll Blender
import os # Does that file exist?

print("")

# controll
samples = int(1e2)
star_size = 0.5

# constants
pi = math.pi
e = math.e
G = 4.302e-3

# variables
sigma = 200
f_0 = 1
R_s = 1e4

# lists
lista = []
listb = []

# arrays
arr_r = np.logspace(-2, 5, num=samples)
arr_rho = np.zeros((samples, 1))

# phi function
def phi(x):
    a = - ( 4 * pi * G * f_0 * R_s ** 3 ) / x
    b = np.log(1. + (x / R_s) )
    c = a * b
    return c

# new phi function
# def phi_new(r, x, y):
#     a = phi(r)
#     b = ( 1 / 2 ) * ...
#     return c

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
xs = np.logspace(-1, 4, samples)

# plot spline and rho
plt.plot(xs, spl(xs), 'g--', lw=2, alpha=0.7)
plt.plot(arr_r, arr_rho, 'b.')

# def create_star(r):
#     bpy.ops.mesh.primitive_cube_add(radius=star_size, location=(r, 0, 0) )

# def create_no_star(r):
    # bpy.ops.mesh.primitive_cone_add(vertices=3, radius1=star_size, radius2=0, depth=star_size, location=(r, 0, -1) )

val_max = max(arr_rho)
val_min = min(arr_rho)

# create new file for every calculation
file_nr = 1
while os.path.isfile('data/' + str(file_nr) + '.txt') == True:
    file_nr += 1

path = 'data/' + str(file_nr) + '.txt'

# ##########
#   1D
# ##########

# print("{:<30}{:<30}".format("spl_max", "spl_min"))
# print("{:<30}{:<30}".format(spl_max, spl_min))
# print("")
# print("{:<20}{:<20}{:<20}".format("r", "spl(xs)[r]", "rand_val" ), end="")
# print("")
#
# for r in range(0, int(1e6), int(1e4)):
#     rand_val = np.random.uniform(spl_min, spl_max, size=1)
#     lista.append(rand_val)
#     print("{:<20}{:<20}{:<20}".format(str(r), str(spl(xs)[r]), str(rand_val) ), end="")
#
#     if rand_val < spl(xs)[r]:
#         print("{:<5}".format("☆"))
#         # create_star(r)
#     else:
#         print("")
#         # create_no_star(r)

print("{:<5}{:<20}{:<20}".format("i", "rand_val", "arr_r[r]" ) )

# cycle through the numbers 1 to 1000
for i in range(1000):

    # generate a random number
    rand_val = np.random.uniform(val_min, val_max, size=1)
    lista.append(rand_val)

    # print the critical information
    print("{:<5}{:<20}".format(str(i) , str(rand_val) ), end="")

    # cycle through the x values
    for r in range(0, len(arr_r)):

        # if the random value is bigger than the x value print the x value
        if rand_val > spl(xs)[r]:

            # print(spl(xs)[r], end="")
            print(arr_r[r])
            listb.append(arr_r[r])

            # open a file th save the results
            with open(path, "a") as data:

                # write the result at the end of the file
                data.write(str(arr_r[r]) + '\n')

            # break and continue cycling eith the next value
            break

            # create_star(r)

        else:
            print("", end="")

# Plot the position
listb.sort(reverse=True)
plt.plot(listb, 'bo')

# Plot the random values
plt.plot(lista, 'ro', alpha=0.7)

# def get_r(x, y, z):
#     return int(math.sqrt(x**2 + y**2 + z**2))


# ##########
#   2D
# ##########

# print("{:<5}{:<5}".format("x", "y"), end=" ")
# print("{:<20}{:<20}{:<20}".format("r", "spl(xs)[r]", "rand_val" ), end="\r")
# for y in range(-35, 35):
#     for x in range(-35, 35):
#         r = get_r(y, x)
#
#         rand_val = np.random.uniform(0, 6e60, size=1)
#
#         print("{:<5}{:<5}".format(y, x), end=" ")
#         print("{:<20}{:<20}{:<20}".format(str(r), str(spl(xs)[int(r)]), str(rand_val) ), end="")
#
#         if rand_val < spl(xs)[int(r)]:
#             print("☆")
#             # create_star(r)
#         else:
#             print(" ")
#             # create_no_star(r)
#
#     print("{:-<80}".format("-"))

# print(" \n\n ")

# for x in range(int(1e15), int(1e16), int(5e15)):
#     for y in range(int(1e15), int(1e16), int(5e15)):
#         r = get_r(x, y)
#
#         rand_val = np.random.uniform(0, 6e60, size=1)
#
#         if rand_val < spl(xs)[int(r)]:
#             print("☆", end="")
#             # print("{:<2}".format(int(r)), end=" ")
#         else:
#             print(" ", end="")
#             # print("{:<2}".format(""), end=" ")
#     print("")


# plot settings
plt.title("Rho")
# plt.legend(['interpolation', 'rho', 'rand'])
plt.xscale('log')
plt.autoscale()
plt.grid()

# display plot
# plt.show()
