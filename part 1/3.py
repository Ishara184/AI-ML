#If

age = int(input("Enter your age: "))
if age < 13 :
    print("child")
elif age < 19 :
    print("teen")
elif age < 50 :
    print("adult")
else:
    print("old")