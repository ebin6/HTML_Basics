"""def Square(num):
    return num**2

print(Square(3))"""

"""d=lambda num:num**2
print(type(d))
print(d(4))

add=lambda a,b:a+b
print(add(45,3))

"""


print(tuple(map(lambda num:num**2 ,[3,7,2,4])))

print(list(filter(lambda a:a%2==0,[56,12,7,9,3,23,8])))


first_name = ["Keith", "Elizabeth","Alex","William"]
last_name = ["Philip","Brown","Smith","Oliver"]

print(list(map(lambda f_name,l_name:f_name+" "+l_name,first_name,last_name)))


from functools import reduce

s=reduce(lambda a,b:a*b,range(1,6))
print(s)




