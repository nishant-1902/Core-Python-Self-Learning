class Employee:
    company ="ITC"
    name = "Defaultname"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of the all languages here is your {self.language} language")


class Programmer(Employee,Coder):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
        
a = Employee()
b = Programmer()

b.show()
b.showlanguage()
b.printLanguages()
