"""def Fun():
    name="Anu" # Local variable
    print(name)

Fun()
"""

number=23
def Add():
    global number
    number=number+2
    print(number)

def Substract():
    global number
    number=number-5
    print(number)

Add()
Substract()
print(number)