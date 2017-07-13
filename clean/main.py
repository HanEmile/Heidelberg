import math # sqrt stuff
import numpy as np # logspace, linspace, arrays, ...
import scipy as sp # ...
import matplotlib.pyplot as plt # plotting
from scipy.interpolate import InterpolatedUnivariateSpline # interpolation / spline
import os # file exists?

# custom imports
import heidelberg as hd # functions
import variables
import constants

# controll
samples = int(1e3)
stars = int(1e3)

# lists
lista = [] # test list nr 1
listb = [] # test list nr 2
axes = ["x", "y", "z"]

# arrays
arr_r = np.logspace(-5, 5, num=samples)
arr_rho = np.zeros((samples, 1))

# generate arr_rho content
for r in range(0, len(arr_r)):
    arr_rho[r] = hd.rho(arr_r[r])

# squeez arrays to 1D
arr_r = np.asarray(arr_r).squeeze()
arr_rho = np.asarray(arr_rho).squeeze()

# interpolation -> spline
x = arr_r
y = arr_rho

spl = InterpolatedUnivariateSpline(x, y)
xs = np.logspace(-5, 5, samples)

plt.plot(spl(xs))

# create new file for every calculation
file_nr = 1
while os.path.isfile('3D/3D_data/' + str(file_nr) + '.csv') == True:
    file_nr += 1

path = '3D/3D_data/' + str(file_nr) + '.csv'

val_max = max(arr_rho)
val_min = min(arr_rho)

list_rand_val = []

def gen_star(i):

    print("{:<3}".format(i))
    temp_arr = [] # create temporary array

    for ax in axes:
        print("{:<3}".format(ax), end="")
        rand_val = np.random.uniform(val_min, val_max, size=1)  # random value
        rand_pm = np.random.uniform(-1, 1, size=1)  # random plus / minus

        for r in range(0, len(arr_r)):

            if rand_val > spl(xs)[r]:
                print("{:<20}".format( arr_r[r] ))
                if rand_pm > 0:
                    temp_arr.append(arr_r[r])
                else:
                    temp_arr.append(-arr_r[r])
                break

            else:
                print("", end="")


    with open(path, "a") as data:
        data.write(str(temp_arr).strip("[]"))
        data.write("\n")

    print("")

for i in range(0, stars):
    gen_star(i)

# Plot the position
# listb.sort(reverse=True)
# plt.plot(listb, 'bo')

# Plot the random values
# plt.plot(lista, 'ro', alpha=0.7)

plt.autoscale()
plt.xscale('log')
plt.grid(ls="--")
plt.legend(["spl", "rho"])

# display plot
# plt.show()
