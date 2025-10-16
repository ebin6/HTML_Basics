"""
course="Python"

for s in course:
    print(s)

for value in [45,23,"Python",5.22]:
    print(value)

student={"name":"Roshin","course":"Python","is_active":True,"age":27}
for s in student:
    print(s," : ",student[s])
"""
"""
number=int(input("Enter the number : "))
for num in range(1,11):
    print(f"{num} * {number} = {num * number}")
"""
"""
s=input("Enter the string : ")  #  "Java"
c_count=dict() # c_count={}
for k in s:  # k = 'v'
    if k in c_count:    # if 'a' in {"J":1,'a':1,'v':1}
        c_count[k]=c_count[k]+1 #c_count['a'] = 2  {"J":1,'a':2,'v':1}  End
    else:
        c_count[k]=1 # c_count['a']=1   {"J":1,'a':1,'v':1}
print(c_count)
for key in c_count:
    print(key," = ",c_count[key])
"""

"""
star=1
for row in range(1,6):
    for sp in range(5-row):
        print(" ",end="")
    for column in range(star):
        print("*",end="")
    star+=2
    print("")
"""

"""num =int(input("Enter the number : "))
fact=1
for k in range(1,num+1):
    fact=fact*k
print(f"Factorial of {num} is {fact}")

"""
# 0 1 1 2 3 5 8 13 21 34
"""sequence_count=10
first,second=0,1
print(first,second,end=" ")
for k in range(sequence_count-2):
    third=first+second
    print(third, end=" ")
    first,second=second,third"""

"""
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
"""
starting_value=int(input("Enter the starting value : "))
ending_value=int(input("Enter the ending value : "))
n=int(input("Enter the number : "))
numbers=[num for num in range(starting_value,ending_value+1) if num%n==0]

print(numbers)