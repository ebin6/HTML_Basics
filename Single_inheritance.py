# class A:
#     def __init__(self):
#         self.title="class A"
#         print("Greetings from class A")
#
# class B(A):
#     def __init__(self):
#         print("Greetings from class B")
#         super().__init__()
#         print(self.title)
#
# ob=B()


# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):
    def set_name(self,n):
        self.name=n
    def sound(self):
        print("Labrador woofs")

lb=Labrador("Tomy")
lb.set_name("Browny")
lb.display_name()
lb.sound()