from numpy import genfromtxt
import bpy
import os

# NIHAO simulation (Wang et al. 2015) data: stars of g1.12e12.01024
# x[kpc] y[kpc] z[kpc] vx[kms^-1] vy[kms^-1] vz[kms^-1]
# 0.011 -0.158 -0.389 95.335 -370.055 -287.738

# controll
star_size = 0.01
step = int(1e4)

g1 = 'data/g1.12e12_stars.txt'
dm1 = 'data/g1.12e12_dm.txt'
g2 = 'data/g2.79e12_stars.txt'
dm2 = 'data/g2.79e12_dm.txt'

# data = genfromtxt(g1, delimiter=' ')
data = genfromtxt(g1, delimiter=' ')
data_dm = genfromtxt(dm1, delimiter=' ')

def create_star(x, y, z):
    bpy.ops.mesh.primitive_cube_add( radius=star_size, location=(x, y, z) )
    bpy.context.object.name = "s"

def create_dark_matter(x, y, z):
    bpy.ops.mesh.primitive_cube_add( radius=star_size, location=(x, y, z) )
    bpy.context.object.name = "dm"

# switch to layer 0 to generate the stars
for i in range(0, len(data), step):
    x = data[i][0]
    y = data[i][1]
    z = data[i][2]

    print("{:<7}{:<7}{:<7}".format(x, y, z), end="")
    print("{:<7}{:<7}{:<3}{:<7}".format(" ", i, " / ", len(data) ))
    create_star(x, y, z)

# switch to layer 1 to generate the dark matter
for i in range(0, len(data_dm), step):
    x = data_dm[i][0]
    y = data_dm[i][1]
    z = data_dm[i][2]

    print("{:<7}{:<7}{:<7}".format(x, y, z), end="")
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
