# combining many array together - stacking
"""
we can combile -
vertically / row wise - vstack()
horizontaly / column wise - hstack()
"""
import numpy as np

arr1 = np.array([1,2,3,4])
arr2 =  np.array([5,6,7,8])

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

# splitting - slipliting array in parts 
"""
np.split() - equal split
np.hsplit() - horizontally split the array
np.vsplit() - vertically split the array

"""
arr3 = np.array([1,2,3,4,5,6])

print(np.split(arr3 , 3))