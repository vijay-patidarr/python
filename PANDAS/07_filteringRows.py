import pandas as pd

data = {
    "name" : ["vijay" , "ajay" , "ravi" , "harish" , "sankar" , "raju" , "nisha" , "harshita"],
    "age" : [19,20,21,24,26,18,20,28],
    "salary" : [20000,40000,20000,60000,30000,43000,54000,12000],
    "performance_score" : [85,75,69,39,90,76,48,39]
}

df = pd.DataFrame(data)
print(df)

print("list of the person with salary greater then 50k \n")

# applying th single econdition here

high_sal = df[df["salary"] > 50000] 

print ("person with high salary")
print(high_sal)

# applying multiple codition on the data frame

salary_new = df[(df["age"] > 20 ) & (df["salary"] > 30000)]

print("persons with salary grater then 30000 and age is grater then 20")
print(salary_new)

# using or condition 

salary_new1 = df[(df["age"] > 25 ) | (df["salary"] > 50000)]
print(salary_new1)