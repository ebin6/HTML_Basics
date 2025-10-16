# class A:
#     def methodA(self,av):
#         self.a=av
#
# class B:
#     def methodB(self,bv):
#         self.b=bv
#
# class C(A,B):
#     def Result(self):
#         print(self.a+self.b)
#
# obj1=C()
# obj1.methodA(10)
# obj1.methodB(20)
# obj1.Result()
#
# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Friendly:
    def greet(self,s):
        print("Friendly!",s)

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")
ob_golden=GoldenRetriever("Micky")
ob_golden.display_name()
ob_golden.greet("Dog")
ob_golden.sound()