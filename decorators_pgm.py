
def loginRequired(fun):
    def wrapper(n,status):
         if status:
             fun(n,status)
         else:
            print("Invalid user")
    return wrapper

def Dashboard(name,is_authenticated):
    print("Welcome ",name)

k=loginRequired(Dashboard)
print(k)
k('Roshin',True)