"""class Student:
    @staticmethod
    def validate(mark):
        if mark>50:
            return "Pass"
        else:
            return "Fail"

    def __init__(self,m):
        self.mark=m

    def result(self):
        print(self.validate(self.mark))

std=Student(67)
std.result()"""

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def new_student(cls,name,age):
        return cls(name,age)

std=Student("Jacob",30)

std2=Student.new_student("Ebin",27)

print(std2.name)