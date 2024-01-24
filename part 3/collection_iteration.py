l = ["apple", "banana", "berry", 45, 56.7, True]

#using while loop
i = 0
while i < len(l):
    print (l[i])
    i += 1

print("\n")

#using for loop
for i in range (0, len(l)):
    print(l[i])

print("\n")

#using for each command
for item in l:
    print(item)