'''a=12
b=3

try:
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by Zero")
except NameError:
    print("Please provide value")
except TypeError:
    print("Please provide integer value")
except Exception as e:
    print("Error : ",e)
else:
    print("Program executed . No errors raised")
finally:
    print("Completed")

    '''

balance=0
try:
    if balance<=0:
        raise TypeError
except TypeError:
    print("Invalid balance amount")
