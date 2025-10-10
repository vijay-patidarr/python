# shape property - how much rows and columns help to underestand the shap of the array
import numpy as np 

arr_2d = np.array([[1,2,3],
           [4,5,6]])

print(arr_2d)
print("shape of the array is ",arr_2d.shape) # give the shape of array how much row and how much column a aarray have

# size - total no. of element in an array
print("size of the array is",arr_2d.size)

# ndim (numbers of dimentions)

arr1 = np.array([[[1,2],[2,3],[3,4],[4,5]]])
print("dimentions of the array are", arr1.ndim)

# dtype - data type of array

print( "type of the array is",arr1.dtype)


# changing the data type of the array using astype


arr2 = np.array([[1.6,2.3,3.3,4.4,5.5]])
print("array before conversion", arr2)
print("before conversion type is ",arr2.dtype)

arr2_new = arr2.astype(int)
print("new array after conversion",arr2_new)
print("type of array after conversion",arr2_new.dtype)