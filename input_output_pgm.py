"""name="Ebin"
age=27

print("My name is ",name,"and I am ",age," years old")"""

name=input("Enter your name : ")
age=int(input("Enter your age : "))
print(type(age))

print("My name is ",name,"and I am ",age," years old")
print(f"My name is {name} and I am {age} years old")
# format is a string method
print("My name is {} and I am {} years old".format(name,age))