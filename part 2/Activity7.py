#function to calculate the factorial of a given number

def fac (num):

    ans = 1

    while num != 0:
        ans = ans * num
        num -= 1
    
    return ans

print("factorail of the number = ", fac(5))