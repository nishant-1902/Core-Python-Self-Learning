f = open("myfile.txt")
print(f.read())
f.close()


# the same code written using with statement:
with open("myfile.txt",'r') as f:
    print(f.read())

# we dont have to close the file     