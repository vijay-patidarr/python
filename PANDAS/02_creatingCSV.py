# creating dataset from the dictionary and storing it in csv o excel etc.

import pandas as pd

data ={
    "name":["raju", "ravi" , "harish"],
    "age" : [19 , 20 , 20 ],
    "city": ["indore", "ratlam", "udaipur"]
}

data_frame = pd.DataFrame(data) # creting data  in frame means store in the sheet

print(data_frame)

# to save this file as csv
data_frame.to_csv("new.csv", index=False)

#save file as excel
data_frame.to_excel("new.xlsx", index=False)

# save file as json
data_frame.to_json("new.json", index=False)