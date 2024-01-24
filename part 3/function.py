#function can return many values

def divide (no1,no2):
    return no1 // no2 , no1 % no2

#want to decalre variables to accept the reurn values 
#no of variables = no of return values
a,b = divide (10,3)
print (a)
print (b)