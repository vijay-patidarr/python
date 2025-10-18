# Vectorization - perform the opertaionn on etire array without using loop and in one time
# in large data this is faster then loops and we also performs large operation faster using it
 
import numpy as np 

arr1 = np.array([10,20,30])
arr2 = np.array([2,4,6])
new_arr = arr1 + arr2
# result of adddimg 2 array  
print(new_arr)