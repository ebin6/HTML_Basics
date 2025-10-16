students={}
def Grade(avg):
    if avg>=95:
        return "A+ grade"
    elif avg>=90:
        return "A grade"
    elif avg>=80:
        return "B grade"
    elif avg>=70:
        return "c grade"
    elif avg>=50:
        return "D grade"
    else:
        return "Failed"
while True:
    marks=[]
    roll_number=int(input("Enter the student roll number : "))
    if roll_number in students:
        print("Roll number exists")
        continue  # Stop current iteration and moves to next iteration
    std_name=input("Enter the student name : ")
    print("Enter the mark of 3 subjects")
    for m in range(1,4):
        score=int(input("Enter the score :"))
        marks=marks+[score]
    avg=sum(marks)/3
    g=Grade(avg)
    students[roll_number]={"name":std_name,"marks":marks,"grade":g}
    choice=input("Do you wish to continue (yes/no) ?")
    if choice!="yes":
        break
print(students)