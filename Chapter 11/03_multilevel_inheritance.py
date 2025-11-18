class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

obj = Employee()
print(obj.a) # prints the a attribute
# print(obj.b) # show the error as no b attribute in employee class    

obj = Programmer()
print(obj.a,obj.b)

obj = Manager()
print(obj.a,obj.b,obj.c)