"""
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
"""
rows=5
for r in range(1,rows+1):
    num=r
    counter=rows-1
    for c in range(r):
        print(num,end=" ")
        num=num+counter
        counter-=1
    print("")
