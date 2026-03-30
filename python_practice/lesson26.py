# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# name = input("Enter your name:")
# age = input("Enter your age:")
# p1 = Person(name, age)
# print(p1.name)
# print(p1.age)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")

name = input("Enter your dog's name:")
age = input("Enter your dog's age:")
d1 = Dog(name, age)
d1.bark()