def is_even(num):
    if num%2==0:
        return True
    else:
        return False

def Prime(num):
    is_prime=True
    if num<=1:
        print("Not Prime")
    else:
        for k in range(2,(num//2)+1):
            if num%k==0:
                is_prime=False
                break
        if is_prime:
            print(num,"is prime")
        else:
            print(num,"is not a prime number")
