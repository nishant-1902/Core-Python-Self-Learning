class Employee():
    lang = "Java"
    salary = "12 lak"

    def getinfo(self):
        print(f"The language is {self.lang} and the salary is {self.salary}")

nishant = Employee()
nishant.lang = "JavaScript"   
nishant.getinfo()