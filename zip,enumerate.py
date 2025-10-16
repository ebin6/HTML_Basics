l=('RAM','model','Storage',7)
k=("16GB","Dell","516GB")
j=("Ebin","Python","Kochi",'Kerala')
print(list(zip(l,k,j)))
for k,v,a in zip(l,k,j):
    print(k,v,a)

for i,v in enumerate(l,start=1):
    print(i,v)