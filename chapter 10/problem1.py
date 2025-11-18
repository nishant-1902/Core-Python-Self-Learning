# 1. Create a class “Programmer” for storing information of few programmers 
#    working at Microsoft.

class programmer():
    company = "Microsoft"

    def __init__(self,name,salary,pin):
        self.name = name 
        self.salary = salary
        self.pin = pin

p1 = programmer("Nishant","40k",415002)
print(p1.name,p1.company,p1.salary,p1.pin)  

p2 = programmer("Shreya","40k",415002)
print(p2.name,p2.company,p2.salary,p2.pin)  

p3 = programmer("Priya","40k",415002)
print(p3.name,p3.company,p3.salary,p3.pin)  

p4 = programmer("Shruti","40k",4150024)
print(p4.name,p4.company,p4.salary,p4.pin)  

p5 = programmer("Shweta","40k",415002)
print(p5.name,p5.company,p5.salary,p5.pin)  