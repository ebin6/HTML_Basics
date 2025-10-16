"""def Fun(**kwargs):
    print(kwargs)
    print(f"My name is {kwargs["n"]} and I am {kwargs["a"]} years old")
    print("Live in ",kwargs['place'])

name="Edwin"
age=27
Fun(a=age,n=name,place="Kochi")

def Add(*number):
    print(number)
    sum=0
    for k in number:
        sum+=k
    return sum
print("sum of number is ",Add(45,3,8,45,1))

"""

def Fun(n,a,p='Kochi'):
    print(f"My name is {n} and I am {a} years old")
    print(p)

name=input("Enter your name : ")
age=int(input("Enter the age : "))

Fun(name,age,"Kollam")