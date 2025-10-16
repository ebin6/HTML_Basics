with open("std_details.txt",'r') as file:
    content=file.readlines()
    for line in content:
        student=line.strip().split('|')
        print("Name :",student[0])
        print("Age :",student[1])
        print("Course :",student[2])
        print("--------------")