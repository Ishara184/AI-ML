# Numpy is a fundermental package for scintific computing python
# It is a library that provides a mutidimensional array objects

#import numpy
import numpy as np

# Array are collections where the data type of all elements are the same
# We can do array based calculations

#create an array
a = np.array([1,2,3,4,5])
print(a)

print("\n")

#datatype specify
a = np.array([1,2,3,4,5],dtype=float)
print(a)

print("\n")

#array dimention
#2D array
print("2D array")
a = np.array([[1,2], [3,4], [5,6]])
print(a)
print("Dimensions = ", a.shape) #print array shape

print("\n")

#3D array
print("3D array")
a = np.array ([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(a, "\n")
print("Dimensions = ", a.shape) #print array shape
print("First dimension of the array =\n",a[0]) #access first element(dimension)
print("First element of the second dimension =\n", a[1][0]) #access first index of second element(dimension)
print("Third index of the 3rd dimension's second element =\n", a[2][1][2])
print("\n")

# arrays initialized special characters(0 & 1)
#zeros
a = np.zeros([10,3], dtype=int)
print(a)
print("\n")
#ones
a = np.ones ([10,3], dtype=int)
print(a)
print("\n")

#generate an array with start and stop parameters set
x = np.arange (1,10)
print(x)
print("\n")

#generate an array of evenly spaced numbers between a given range
x = np.linspace (1,10,5)
print(x)
print("\n")

#slicing
a = np.array ([10,20,30,40,50,60,70,80,90,100])
print(a)
print(a[0:4]) # print first element to fourth element
print(a[2:]) # print all the elements from third element onward
print(a[:7]) # print all the elements upto 7th element
print("\n")

#direct array manipulation
a1 = np.array([10,20,30,40,50])
a2 = np.array([2,4,6,8,10])

c = a1 + a2
print(c)
c = a1 - a2
print(c)
c = a1 * a2
print(c)
c = a1 / a2
print(c)
c = a1 * 2
print(c)
c = a2 ** 2
print(c)
c = a1 * 2 + a2
print(c)

print("\n")

#specific functions
y = np.array([10,20,30,40,50])
print(y.sum())
print(y.min())
print(y.max())
print(y.mean())

print("\n")
