while True:
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
    choice=input("Enter your choice : ")
    match choice:
        case '1' | "+":
            print(a+b)
        case '2' | "-":
            print(a-b)
        case '3' | "*":
            print(a*b)
        case '4' | "/":
            print(a/b)
        case __:
            print("Invalid input")
    c=input("Do you wish to continue (yes/no) ?")
    if c!="yes":
        break


