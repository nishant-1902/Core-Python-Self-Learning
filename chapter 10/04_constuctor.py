class Employee():
    lang = "Java"
    salary = "12 lak"

    def __init__(self,name,salary,lang):
        self.name = name
        self.salary = salary
        self.lang = lang

    def getinfo(self):
        print(f"The language is {self.lang} and the salary is {self.salary}")

nishant = Employee("Nishant",12000000,"Python")
nishant.lang = "JavaScript"
print(nishant.name,nishant.salary,nishant.lang)   
nishant.getinfo()