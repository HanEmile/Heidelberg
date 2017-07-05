import bpy
import math
import numpy as np

print("\n")

# variables
bound = 5
circle_radius = 10
obj_size = 0.01

# lists
dist_list = []

for i in range(-bound, bound):
    for j in range(-bound, bound):
        for k in range(-bound, bound):
            distance_to_zero = math.sqrt(math.pow(i, 2) + math.pow(j, 2))
            randomgen = np.random.uniform(0, 1, size=1)
            distribution = distance_to_zero * randomgen
            dist_list.append(distribution)

            # bpy.ops.mesh.primitive_cube_add(radius=0.001, location=(i, j, k))
            # bpy.ops.mesh.primitive_cone_add(radius1=1, radius2=0, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            bpy.ops.mesh.primitive_cone_add(vertices=3, radius1=obj_size, radius2=0, depth=obj_size, location=(i, j, k))
