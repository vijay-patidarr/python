import numpy as np 

prices = np.array([100,200,399])
discount = 10 # scaler single value 

final_prices = prices - (prices*discount)/100
print(final_prices)

# operation with single value 
array1 = np.array([10,20,30,40,50])
result = array1*2
print(result)

# operation of 1d and 2d array 

arr1 = np.array([[10,20,30], [40,5,60]])
arr2 = np.array([2,4,6])
new_arr = arr1 + arr2
# result of adddimg 2 array  
print(new_arr)

"""
error case 
arr1 = np.array([[10,20,30], [40,5,60]])
arr2 = np.array([2,4,]) # here in this line there is only 2 element not match the condition and give error
new_arr = arr1 + arr2

we use reshape and solve this issue 
"""