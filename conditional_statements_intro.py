"""
Syntax

if condition:
   statements

"""

"""age=int(input("Enter your age : "))
if age>=18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
"""

"""mark=int(input("Enter your mark : "))
if mark>=95:
    print("Excellent")
    print("You secured A+")
elif mark>=75:
    print("Good Job")
    print("You secured B grade")
elif mark>=50:
    print("You secured c grade")
else:
    print("Keep practicing")
"""
"""
age=int(input("Enter your age : "))

if age>=60:
    c = input("Do you have membership card (yes / no) : ")
    is_member = True if c == "yes" else False
    if is_member:
        print("Congrats you got 30% discount")
    else:
        print("You are eligible for 10% discount")
else:
    print("Not eligible for discount")
"""

number={
1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",
7:"Seven",8:"Eight",9:"Nine",10:"Ten",
}

num=int(input("Enter any digit between 1 - 10 : "))
if num in number:
    print(number[num])
else:
    print("Error")