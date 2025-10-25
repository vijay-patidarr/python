# creating a data frame selecting a column and filtering it 
import pandas as pd

data = {
    "name" : ["vijay" , "ajay" , "ravi" , "harish" , "sankar" , "raju" , "nisha" , "harshita"],
    "age" : [19,20,21,24,26,18,20,28],
    "salary" : [20000,40000,20000,60000,30000,43000,54000,12000],
    "performance_score" : [85,75,69,39,90,76,48,39]
}

df = pd.DataFrame(data)
print(df)

print("names(single column return series)")

print(df["name"])

print("names and age (returns a data set) ")

subset = df[["name", "age"]]

print(subset)