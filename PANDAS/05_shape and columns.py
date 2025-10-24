"""
before manipulating we have 2 questions
1- how big is your data set 
2- what are the names of columns

shape and column attributte 
shape -give the no.of rows and the no.of column in the data set(attribute return tupple with 2 values )
column - give the name of the columns of the data  (attribute return name of column as as an index)
"""
import pandas as pd

data = {
    "name" : ["vijay" , "ajay" , "ravi" , "harish" , "sankar" , "raju" , "nisha" , "harshita"],
    "age" : [19,20,21,24,26,18,20,28],
    "salary" : [20000,40000,20000,60000,30000,43000,54000,12000],
    "performance_score" : [85,75,69,39,90,76,48,39]
}

df = pd.DataFrame(data)
print(df)

print(f"shape : {df.shape}")
print(f"columns name :{df.columns}")