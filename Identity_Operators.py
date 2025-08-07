x=78
y=78

print(x==y)
print(id(x))
print(id(y))

print(id(y))
print(x is y)
print("_________")
l=[34,"Ebin",8]
j=[34,"Ebin",8]

print(id(l))
print(id(j))

print(l is j)

print(l == j)
print("_________")


l=[34,"Ebin",8]
j=l    # j=[34,"Ebin",8]

print(id(l))
print(id(j))