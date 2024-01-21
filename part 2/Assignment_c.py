# b) Create a python program to input marks of 10 students and print the maximum mark, minimum mark and average mark of the students.

mark = int(input("Enter the marks of the student: "))
max = 0
min = mark
i = 1
sum = 0

while i < 10:
    
    if mark > max:
        max = mark

    if mark < min:
        min = mark

    sum = sum + mark

    i += 1
    mark = int(input("Enter the marks of the student: "))
    
print ("Maximum marks = ", max)
print ("Minimum marks = ", min)
print ("Average marks = ", sum/10 )



