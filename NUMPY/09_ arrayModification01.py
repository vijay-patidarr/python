# insert a value in a array
# np.array(arr , index , value , axis)
# arr - array in which you have to insert
# index - on which index you have to add the value 
# vlaue - value you have to insert in the array
# axis = none if we have to change in the flattern versison of array
# axis = 0 want to change in the row 1 if we have to chage in the column

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])
print(arr)
new_arr = np.insert(arr, 3,100) # axis is set as 0 default
print(new_arr)

# inserting element in the 2d array

arr1 = np.array([[1,2] , [3,4]])
print(arr1)

arr1_new = np.insert(arr1 , 1 , [5,6] , axis=0)
print(arr1_new)


# append - adding data in the end of the array

arr2 = np.array([1,2,3,4,])

print(np.append(arr2 ,[5,6,7] ))
# np.append(arr , value ) arr - in array we have to change , value - value we have to append 

