# d)  Write a program to input a series of numbers terminated by -999. Calculate and print the sum of the numbers entered. 

sum = 0
print("Enter -999 to stop the process")
num = int(input("Enter number: "))

while num != -999:
    sum = sum + num
    num = int(input("Enter number: "))

print ("Sum of you entered numbers= ", sum)