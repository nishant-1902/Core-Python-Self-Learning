# write a program using function to find a greatest of three numbers
a = 10
b = 20 
c = 30

def greater(a,b,c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c
print(greater(a,b,c))