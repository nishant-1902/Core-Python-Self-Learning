'''write a python program to print the contents of a directory using the os module. search online for the function which does that '''

import os
# select the directory whose content you want to list
directory_path = '/your/directory/path'

# use the os module to list the directory content
contents = os.listdir('/fortune cloud WD')

# print the contents of the directory
for item in contents:
    print(item)

