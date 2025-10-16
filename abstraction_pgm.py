from abc import ABC,abstractmethod


class A(ABC):
    @abstractmethod
    def greeting(self):
        pass

class B(A):
    def greeting(self):
        print("Hello")

ob=B()
ob.greeting()