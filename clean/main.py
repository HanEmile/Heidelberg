import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
import os

# custom imports
import heidelberg as hd
import variables
import constants

# controll
samples = int(1e2)

# lists
lista = []
listb = []

# arrays
arr_r = np.logspace(-2, 5, num=samples)
arr_rho = np.zeros((samples, 1))

# generate arr_rho content
for r in range(samples):
    arr_rho[r] = hd.rho(arr_r[r])

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

# create new file for every calculation
file_nr = 1
while os.path.isfile('data/' + str(file_nr) + '.txt') == True:
    file_nr += 1

path = 'data/' + str(file_nr) + '.txt'

val_max = max(arr_rho)
val_min = min(arr_rho)

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

plt.autoscale()
plt.xscale('log')
plt.grid()
plt.show()

# print(hd.rho(42))
