# to convert multi dimentional array in 1-d array 
# .ravel() returns a view
# .flatteen() returns a copy

import numpy as np 

arr = np.array([[1,2,3,] , [4,5,6,]])
print(arr.ravel())
print(arr.flatten())