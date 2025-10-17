# Array Concatination - adding two different array 
"""
syntaxt

np.concatiante((arr1 , arr2), axis )

axis = 0 veriitival satacking 
axis = 1 horizontal stacking 
"""

import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

arr3 = np.concatenate((arr1,arr2))
print(arr3)


# removing element of the array
"""
np.delete(array, index , axis=none)
axis = none is used for flattern array
"""

arrr = np.array([1,2,3,4,5])
print(arrr)
print(np.delete(arrr , 0))

# how to delete a element from 2d array

arrr1 = np.array([[1,2,3],[4,5,6]])
delete_arr = np.delete(arrr1 , 0, axis=0)
print(delete_arr)