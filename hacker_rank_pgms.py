"""
num=int(input("Enter the number : "))

if num%2==0:
    if 2<=num<=5:
        print("Not Weird")
    elif 6<=num<=20:
        print("Weird")
    elif num>20:
        print("Not Weird")

else:
    print("Weird")
"""
year = int(input("Enter the year : "))

if year%4==0 and year%100!=0 or year%400==0:
    print(year,"is leap year")
else:
    print(year,"is not a leap year")
