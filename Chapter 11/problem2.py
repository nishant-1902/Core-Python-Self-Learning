# 2.create class 'pets' from a class animal and further create a class dog from pets. add a method
# bark to class dog.

class Animal:
    pass

class Pets(Animal):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")
    pass

d = Dog()
d.bark()