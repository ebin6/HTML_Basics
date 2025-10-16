s={45,3,8,12,"Ebin",7.2}
s.add("Kochi")
print("Add : ",s)
s.update(['OneTeam',67])
print(s)
s.remove('Ebin')
print("After remove : ",s)
s.discard('Rohith')
print(s)
print(s.pop())
print("pop ",s)

set1={56,'kochi',12,'Python'}
set2={12,'kochi',56,'Java',"Python"}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

print(set2.issubset(set1))

