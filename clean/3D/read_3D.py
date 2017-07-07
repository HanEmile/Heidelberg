from numpy import genfromtxt
import sys
# from gen_3D import path

path = '3D_data/' + str(sys.argv[1]) + '.csv'

# read the data
my_data = genfromtxt(path, delimiter=',')
print(my_data)
