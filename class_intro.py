class Students:
    institute='OneTeam' # class attribute
    def __init__(self,n,a):
        self.name=n
        self.age=a

    def display(self,p):
        self.place=p
        print(f"Your name is {self.name} and you are {self.age} years old")

st1=Students("Arjun",28)
st2=Students("Anu",29)
obj=Students("Ebin",27)
obj.display('Kochi')
print(obj.place)


