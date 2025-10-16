class BaseClass:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
class Child1(BaseClass):
    def displayC1(self):
        print(self.a)
class Child2(BaseClass):
    def add(self):
        print(self.a+self.b+self.c)
c1=Child1()
c1.displayC1()

c2=Child2()
c2.add()

print(type(c2))