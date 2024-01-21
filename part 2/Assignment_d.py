# c) Create a program to input five marks of a student and display the grades. 

#           • Mark > 75 – A 

#           • Mark 65 to 75 – B 

#           • Mark 55 to 64 – C 

#           • Mark 45 to 54 – S 

#           • Mark < 45 – F


i = 0

while i < 5:
    mark = int(input("Enter student mark : "))

    if mark >= 75:
        print ("A")
    elif mark >= 65:
        print ("B")
    elif mark >= 55:
        print ("C")
    elif mark >= 45:
        print ("S")
    else:
        print ("F")

    i += 1
