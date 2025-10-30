import pandas as pd

data = {
    "name" : ["vijay" , "ajay" , "ravi" , "harish" , "sankar" , "raju" , "nisha" , "harshita"],
    "age" : [19,20,21,24,26,18,20,28],
    "salary" : [20000,40000,20000,60000,30000,43000,54000,12000],
    "performance_score" : [85,75,69,39,90,76,48,39]
}

df = pd.DataFrame(data)
print(df)

# adding column via assignment --> df = ["column_name"] = some data for column

df["Bonus"] = df["salary"] * 0.1

print(df)

# using insert() method
#  we can add a column at preciese loction using insert 
# syntax df.insert(location, column_name, data)

df.insert(0 , "id" , ["001","002","003","004","005","006","007","008"])
print("list with id of all persons")
print(df)