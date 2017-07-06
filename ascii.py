import os # Does that file exist?

file_nr = 1
while os.path.isfile('data/' + str(file_nr) + '.txt') == True:
    file_nr += 1

path = 'data/' + str(file_nr - 1) + '.txt'

with open(path, "r") as data:
    content = data.readlines()

    for line in content:
        line.rstrip('\n')
        print(line, end="")
