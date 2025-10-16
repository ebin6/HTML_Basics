numbers=[34,1,98,4,3]

length=len(numbers)

for k in range(length):
    swap=False
    for j in range(length-k-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
            swap=True
    if swap==False:
        break
print(numbers)
