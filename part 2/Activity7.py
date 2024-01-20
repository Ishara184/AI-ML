#function to calculate the factorial of a given number

num = int(input("Enter a num: "))
count = num
ans = 1

while count != 0:
    ans = ans * count
    count -= 1

print("factorail of the number = ", ans)