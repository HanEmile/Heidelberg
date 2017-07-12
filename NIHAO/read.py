from numpy import genfromtxt
import bpy
import os
# from multiprocessing import Pool


# First three lines of a data-set
#
# NIHAO simulation (Wang et al. 2015) data: stars of g1.12e12.01024
# x[kpc] y[kpc] z[kpc] vx[kms^-1] vy[kms^-1] vz[kms^-1]
# 0.011 -0.158 -0.389 95.335 -370.055 -287.738
#
# Blender 1 length-unit -> 1 kpc

# controll
star_size = 0.01
step = int(1e5) # int(5e3) # int(5e2)
time_step = 1.5e14 # s
parsec = 3.086e16 # m

g1 = 'data/g1.12e12_stars.txt'
dm1 = 'data/g1.12e12_dm.txt'
g2 = 'data/g2.79e12_stars.txt'
dm2 = 'data/g2.79e12_dm.txt'

# create star at the given coordiantes
def create_star(x, y, z):
    bpy.ops.mesh.primitive_cube_add( radius=star_size, location=(x, y, z) )
    bpy.context.object.name = "s" + str(i)

# create "dark matter" at the given coordinates
def create_dark_matter(x, y, z):
    bpy.ops.mesh.primitive_cube_add( radius=star_size, location=(x, y, z) )
    bpy.context.object.name = "dm" + str(i)

# get data from files
data = genfromtxt(g2, delimiter=' ')
data_dm = genfromtxt(dm2, delimiter=' ')

# define sce
sce = bpy.context.scene
sce.frame_set(0)

# create stars
for i in range(0, len(data), step):
    # get the position data of the star
    x = data[i][0]
    y = data[i][1]
    z = data[i][2]

    # print some information
    print("{:<10}{:<10}{:<10}".format(x, y, z), end="")
    print("{:<7}{:<7}{:<3}{:<7}".format(" ", i, " / ", len(data) ))

    # create the star
    create_star(x, y, z)

# create dark matter
for i in range(0, len(data_dm), step):
    x = data_dm[i][0]
    y = data_dm[i][1]
    z = data_dm[i][2]

    print("{:<10}{:<10}{:<10}".format(x, y, z), end="")
    print("{:<7}{:<7}{:<3}{:<7}".format(" ", i, " / ", len(data_dm) ))
    create_dark_matter(x, y, z)

file_nr = 1
# cycle through possible files
while os.path.isfile('blender_files/' + str(file_nr) + '.blend') == True:
    # if file allready exists, see if the next one is available
    file_nr += 1

blender_file_path = 'blender_files/' + str(file_nr) + '.blend'
print(blender_file_path)

# save the blender file
bpy.ops.wm.save_as_mainfile(filepath=blender_file_path)
