import re
# W ---  Special characters required


pattern=r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{8,}$"
password=input("Enter your password : ")

if re.match(pattern,password):
    print("Valid")
else:
    print("Not valid")
