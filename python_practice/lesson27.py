class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f"{self.name} got Grade {self.grade}")


name = input("Enter your name:")
age = input("Enter your age:") 
grade = input("Enter your grade:")
s1 = Student(name, age, grade)
s1.study()