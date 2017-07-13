from numpy import genfromtxt
import numpy as np
import math
import time
# import bpy
import os

# controll
star_size = 0.1

# variables
sigma = 200
f_0 = 0.1
R_s = 1e4

# constants
pi = math.pi
e = math.e
G = 4.302e-3

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

def gen_stars(stars, print_time=False):
    stars = int(stars)

    time_start = time.time()

    # lists
    listrho = []
    arr_stars = np.zeros((stars, 3))
    arr_stars_keep = []

    # range for stars to be created in
    range_min = -int(1e5)

    # create new file for every calculation
    file_nr = 1
    while os.path.isfile('data/' + str(file_nr) + '.csv') == True:
        file_nr += 1

        path = 'data/' + str(file_nr) + '.csv'
    print("path: " + str(path))

    range_min = -int(1e6)
    range_max = int(1e6)

    # create random stars
    for r in range(0, stars):
        x = np.random.uniform(range_min, range_max, size=1)
        y = np.random.uniform(range_min, range_max, size=1)
        z = np.random.uniform(range_min, range_max, size=1)
        rand_val = np.random.uniform(0, rho(0), size=1)

        r = math.sqrt(x**2 + y**2 + z**2)
        if rand_val < rho(r):
            with open(path, "a") as data:
                data.write(str(x).strip("[]") + "," + str(y).strip("[]") + "," + str(z).strip("[]") + "\n")


    # # create random stars
    # for r in range(0, stars):
    #     arr_stars[r][0] = np.random.uniform(range_min, range_max, size=1)
    #     arr_stars[r][1] = np.random.uniform(range_min, range_max, size=1)
    #     arr_stars[r][2] = np.random.uniform(range_min, range_max, size=1)

    # # apply rho function
    # for i in range(0, len(arr_stars)):
    #     x = round(arr_stars[i][0], 2)
    #     y = round(arr_stars[i][1], 2)
    #     z = round(arr_stars[i][2], 2)
    #     r = round(math.sqrt(x**2 + y**2 + z**2), 2)
    #     rho_val = rho(r)
    #
    #     listrho.append(rho_val)

    # # get min / max value of rho
    # min_list_rho = min(listrho)
    # max_list_rho = max(listrho)

    # # generation of arr_stars_keep array
    # for i in range(len(listrho)):
    #     rand_value = np.random.uniform(min_list_rho, max_list_rho)
    #
    #     # rejection sampling
    #     if rand_value < listrho[i]:
    #         with open(path, "a") as data:
    #             data.write(str(arr_stars[i][0]) + "," + str(arr_stars[i][1]) + "," + str(arr_stars[i][2]) + "\n")

    time_all = time.time() - time_start

    if print_time == True:
        print("time: " + str(round(time_all, 2)) + " s")

# generate n stars
gen_stars(1e6, True)

# create star at the given coordiantes
# def create_star(x, y, z):
#     bpy.ops.mesh.primitive_cube_add( radius=star_size, location=(x, y, z) )
#     bpy.context.object.name = "s" + str(i)

# # read from newest file
# file_nr = 1
# while os.path.isfile('data/' + str(file_nr) + '.csv') == True:
#     file_nr += 1
#
#     path = 'data/' + str(file_nr - 1) + '.csv'

# data = genfromtxt(path, delimiter=',')

# create stars
# for i in range(0, len(data)):
    # get the position data of the star
    # x = data[i][0]
    # y = data[i][1]
    # z = data[i][2]

    # create the star
    # create_star(x, y, z)

# file_nr = 1
# # cycle through possible files
# while os.path.isfile('blender_files/' + str(file_nr) + '.blend') == True:
#     # if file allready exists, see if the next one is available
#     file_nr += 1
#
# blender_file_path = 'blender_files/' + str(file_nr) + '.blend'
# print("blender save-path: " + blender_file_path)

# save the blender file
# bpy.ops.wm.save_as_mainfile(filepath=blender_file_path)

################################################################################

# # Benchmarks:
# # 1e5 Stars: ~2.93   s
# # 1e6 Stars: ~29.38  s
# # 1e7 Stars: ~315.67  s
