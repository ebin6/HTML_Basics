student={"name":"Aleena","age":27,6:'Python'}

print(student.get('place',"No found"))

student.update({"palce":'Kochi'})

d=student.pop(6)
print("Deleted value is : ",d)
print(student)
print(student.popitem())
print("Dictionary after popitem : ",student)
print(student.items())

for k,v in student.items():
    print(k,v)

l=('RAM','model','Storage',7)
k="Unknow"
laptop=dict.fromkeys(l,k)
print(laptop)

