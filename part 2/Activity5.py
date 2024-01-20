#find sum of 10 numbers user entered

count = 0
sum = 0

while count < 10:
    num = int(input("Enter the number: "))
    sum = sum + num
    count += 1
    
print ("Sum = ", sum)