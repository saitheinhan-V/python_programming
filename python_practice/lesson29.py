class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._grade = None

    def get_grade(self):
        return self._grade
    
    def set_grade(self, mark):
        if mark >= 80 and mark <= 100:
            self._grade = "A"
        elif mark >= 70 and mark < 80:
            self._grade = "B"
        elif mark >= 60 and mark <70:
            self._grade = "C"
        elif mark >= 50 and mark < 60:
            self._grade = "D"
        else:
            self._grade = "F"

name = input("Enter your name:")
age = input("Enter your age:")
s1 = Student(name, age)
mark = int(input("Enter your mark:"))
s1.set_grade(mark)
print(f"{s1.name} got Grade {s1.get_grade()}")