class A:
    def greetings(self):
        print("Good Evening")

class B(A):
    def greetings(self):
        print("Hello from class B")

ob=B()
ob.greetings()