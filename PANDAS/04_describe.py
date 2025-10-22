# step 1 - create a sample data frame
import pandas as pd 

data = {
    "name" : ["vijay" , "ajay" , "ravi" , "harish" , "sankar" , "raju" , "nisha" , "harshita"],
    "age" : [19,20,21,24,26,18,20,28],
    "salary" : [20000,40000,20000,60000,30000,43000,54000,12000],
    "performance_score" : [85,75,69,39,90,76,48,39]
}

data_frame = pd.DataFrame(data)
print("sample data frame")
print(data_frame)
print("\n discriptibe statemenet")
print(data_frame.describe())
"""
 discriptibe statemenet
             age        salary  performance_score
count   8.000000      8.000000           8.000000
mean   22.000000  34875.000000          65.125000
std     3.585686  17233.169844          20.364097
min    18.000000  12000.000000          39.000000
25%    19.750000  20000.000000          45.750000
50%    20.500000  35000.000000          72.000000
75%    24.500000  45750.000000          78.250000
max    28.000000  60000.000000          90.000000
"""