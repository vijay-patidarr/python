import numpy as np

# creating a array 

# one-dimentional array
marks = np.array([1,2,3,4,5,6]) # calling aarray function and creating a array of a list
print("this is one dimentional array")
print(marks)

# two dimentional array
num = np.array([[1,2,3],
               [4,5,6],])
print("this is two dimentional array")
print(num)

# multi dimentional array
num1 = np.array([[[1,2,3],[1,2,3]],
                 [[3,2,1],[3,2,1]]])
print("this is multi dimentional array")
print(num1)

# creating a array with default values we crete a empty array and fill it in future 

arr1 = np.zeros(3) # this is one dimentional array
print("with default values 1D array \n ",arr1)


arr2 = np.zeros((3,3)) # this is 2D array with default value
print("with default values 2D array \n ",arr2)

arr3 = np.ones((2,3))
print("print one as a default value \n ",arr3)

#full function - create a array with a custom default value you want

arr4 = np.full((2,3),4)
# full((shape), value )
print("this is a array wwith custom default value 4 \n",arr4)

# creting sequences of number 

arr5 = np.arange(2,12,2)
# arange(start,stop,step) work like range in python
print("here is the array from 2 to 10 with 2 step \n",arr5)

# creatng a identity matrices
# matrices with once on the digonal and other values are zero

identity_matrix = np.eye(3)
# eye(size of matrix)

print("here ie the identity matrix \n",identity_matrix) #this is the print line