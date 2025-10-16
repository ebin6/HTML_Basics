from mypackage import Maths_module,mod2


num=int(input("Enter the number : "))
if Maths_module.is_even(num):
    print(num,"is even")
else:
    print(num,"is Odd")

mod2.Prime(78)