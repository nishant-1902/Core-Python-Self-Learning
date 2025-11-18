class Employee():
    lang = "Python" # this is class attribute
    salary = 1200000

harry = Employee()
harry.lang = "JavaScript" # this is instance attribute
print(harry.lang,harry.salary)    