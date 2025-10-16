import copy

l=[12,4,6,'Python']

l2=copy.copy(l)

print(id(l))
print(id(l2))

l2[0]=10
print(l)
print(l2)
