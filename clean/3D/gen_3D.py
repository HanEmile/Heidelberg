import numpy as np
from numpy import genfromtxt
import os


file_nr = 1
# cycle through possible files
while os.path.isfile('3D_data/' + str(file_nr) + '.csv') == True:
    # if file allready exists, see if the next one is available
    file_nr += 1

print(file_nr)

###########
# T E S T #
###########
path = '3D_data/' + str(file_nr) + '.csv'

print(path)
print("")

for i in range(0, 20):

    # generate random coordinates (x, y, z)
    rand_val = np.random.uniform(0, 10, size=3)

    # round the coordinates for easy further use
    value_0 = int(round(rand_val[0], 0))
    value_1 = int(round(rand_val[1], 0))
    value_2 = int(round(rand_val[2], 0))

    value_0 = str(value_0) + ','
    value_1 = str(value_1) + ','
    value_2 = str(value_2) + '\n'

    # open a file th save the results
    with open(path, "a") as data:

        # write the result at the end of the file
        data.write(value_0)
        data.write(value_1)
        data.write(value_2)

print("")
