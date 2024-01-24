#import the module
import test as t

t.hello()
a,b,c,d = t.calc (40,2) #---- values for the elements of the function
#   |
#variables for store return values
print(a)
print(b)
print(c)
print(d)
print("\n")

#import a specific function and given it an alias(rename)
from test import hello as greet
greet()
print("\n")