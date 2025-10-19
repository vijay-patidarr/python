# importing pandas library
import pandas as pd

# reading data from existing file
"""
reading the csv file 

data = pd.read_csv("C:\code\Python\PANDAS\sales_data_sample.csv",  encoding="latin1")
print(data) # gives unicode decode error we have 2 type of incodings utf-8 and latin1

"""

"""
read the excel file 
data = pd.read_excel("C:\code\Python\PANDAS\SampleSuperstore.xlsx")
print(data)
"""

"""
to read the json file data
data = pd.read_json("C:\code\Python\PANDAS\sample_Data.json")
print(data)
"""

# gcsfs libraray is used to read the cloud data