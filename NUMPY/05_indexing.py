# Indexing - pick up one element 
# slicing - more thhen one elemet pick 
# fancy indexing 
# boolean masking 
import numpy as np

# numpy use zero based indexing and we also use negetive indexing use -1 as first value 

arr = np.array([10,20,30,40,50])
print(arr[0]) # example of positive indexing
print(arr[2])
print(arr[-1]) # example of negetive indexing

# slicing - pick up the specific part odf the array
# [start:stop:step]
print(arr[1:4:1]) # if we set start as -1 then it run in reverse order
# step value is default one 
print(arr[:4]) # here start automaticly set to 0 and stop is 4 and step is one default

print(arr[::2]) # run at step size of 2 and print full array

# FANCY INDEXING 

print(arr[[0, 2, 4]])