"""
Numbers
   int  --->   int()
   float --->  float()
   complex   ---> complex()

String

List   -->  Ordered  , Mutable , []   --> list()

Tuple  -->  Ordered , Immutable , ()  ---> tuple()

Set   -->   Unordered , Elements in set must be unique , {}  --> set()

Dictionary --> {} , Key : Value pairs   --->  dict()

Boolean   --> True , False
"""
age= 27
p=3.14
c=7j

name='Ebin'



my_list=[45,"Ebin",12,7.3]
#        0    1    2   3

print(my_list[2])

my_list[2]=6
print(my_list)



my_tuple=(45,"Ebin",12,7.3)
#        0    1    2   3
print(my_tuple[2])


print(my_tuple)


print("Set ")

s={23,"Ebin","Python",34.2,7,34.2,"Ebin"}
print(s)
print(type(s))
  

student={'name':"Rohith","age":23,4:"Python","Hobbies":["Coding","Cycling","Football"]}

print(student['name'])
print(student['Hobbies'][1])
student["age"]=25
print(student)


