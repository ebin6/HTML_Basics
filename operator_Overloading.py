class A:
    def __init__(self,vara,varb):
        self.a=vara
        self.b=varb

    def __add__(self, other):
        return self.a+other.a,self.b+other.b


ob1=A(23,1)
ob2=A(6,5)

print(ob1+ob2)
