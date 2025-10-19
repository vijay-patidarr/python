# missing value 
"""
np.isnan - detact missing values (nan - not a number)
np._nan_to_nam() - replace missing value with another value 
np.isinf() - detact infinite values 
"""
import numpy as np

# isnan syntax - np.isnan(array)

arr = np.array([1,np.nan , 2 ,3 ,4 ,5 ,np.nan ,7 ,])

print(np.isnan(arr))

# print(np.nan == np.nan)  we can  not compare it directly 

# np.nan_to_num(array , nan=value )

print(np.nan_to_num(arr, nan = 1000))

# np.isinf(array) - used for the large value or infinite value which exceeds the python 

arr1 = np.array([ 10 , 20 , np.inf , 30 , -np.inf])
print(np.isinf(arr1))

# replacing the infinite values 
replaced = np.nan_to_num(arr1 , posinf = 100 , neginf=100)

print(replaced)