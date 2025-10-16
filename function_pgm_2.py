"""def Fun():
    course="Python"
    def nf():
        nonlocal course
        course=course+" Full Stack"
        print(course)
        print("Hi")
    nf()
    print("Outer fun")
    print(course)

Fun()"""

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  print("Value of x before function call",x)
  myfunc2()
  return x


print(myfunc1())