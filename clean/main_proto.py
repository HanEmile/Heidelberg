import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
import os
from multiprocessing import Pool

# custom imports
import heidelberg as hd
import variables
import constants

#####
# README!
# generate eaven distibuted coordinates and insert them into the rho function
# to get a rho-value. Compare that value to a random value to see if a star
# should be generated
#####

# controll
samples = int(1e3)
stars = int(1e3)

# lists / arrays
lista = []
arr_rand_pos = np.zeros((stars, 3))

# create new file for every calculation
file_nr = 1
while os.path.isfile('3D/3D_data/' + str(file_nr) + '.csv') == True:
    file_nr += 1

path = '3D/3D_data/' + str(file_nr) + '.csv'
print(path)

def gen_star(star_nr):
    temp_arr = np.zeros((3))

    for axis in range(0, 3):
        rand_val = np.random.uniform(int(1e1), int(1e12), size=1)
        arr_rand_pos[star_nr][axis] = rand_val

    x = arr_rand_pos[star_nr][0]
    y = arr_rand_pos[star_nr][1]
    z = arr_rand_pos[star_nr][2]

    temp_arr[0] = x
    temp_arr[1] = y
    temp_arr[2] = z
    # print(temp_arr)

    rand_val_check = np.random.uniform(0, 20, size=1)
    print("{:<20}{:<20}".format(str(rand_val_check), str(hd.rho3d(x, y, z)) ))

    if rand_val_check > hd.rho3d(x, y, z):
        with open(path, "a") as data:
            data.write( str(temp_arr[0]).strip("[]") + "," )
            data.write( str(temp_arr[1]).strip("[]") + "," )
            data.write( str(temp_arr[2]).strip("[]") )

            data.write("\n")

for star in range(0, stars):
    gen_star(star)

print("")

# arr_log = np.logspace(1, 7, int(1e5))
# print(len(arr_log))
#
# for i in arr_log:
#     print("{:<10}{:<20}".format(i, hd.rho3d(i, i, i)))
#     lista.append(hd.rho3d(i, i, i))
#
# plt.plot(lista)
# plt.xscale('log')
# plt.show()
