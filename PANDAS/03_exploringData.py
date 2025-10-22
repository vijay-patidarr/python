# understanding the structure of the data how many rows are ethere and how many columns are there and how they are arranged 

# to view rows 
# we have to type of 2 methods head() and tail provided by pandas datframe object
"""
head(n) - give the data of n no. of rows from top if there is no no. given then it defult give 5 rows 
tail(n) - give the data of n no. of rows from bottom if there is no no. given then it defult give 5 rows  
""" 

import pandas as pd

data = pd.read_excel("C:\code\Python\PANDAS\SampleSuperstore.xlsx")


# print("print the first 10 rows : \n",data.head(10))

# print("print the first 10 rows :\n",data.tail(10))

print("desplay the information of the data \n")

print(data.info())