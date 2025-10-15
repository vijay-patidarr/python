# reshaping means changing the shape of the array without changing the data 
# arr.reshape() -- after conversion no. of element remains same
# reshape(rows , columns) -  specifies a new shape , if dimensions match  then only we can reshape a  arrray

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

reshaped = arr.reshape(3,3) #reshaping does not crete a copy it affect the old array
print(reshaped)