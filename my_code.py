import pandas as pd

import os

data={

  "name": ["Hasnat","Maruf","Momin"],
  "Age":[23,24,22],
  "address": ["bog","raj","kus"]

}


df=pd.DataFrame(data)


# adding new row 
df.loc[len(df.index)]={"name": "GF1","Age":25,"address": "nator"}


# adding new row 
# df.log[len(df.index)]={"name": "V3","Age":30,"address": "city1"}



# make dir 

os.makedirs("data",exist_ok=True)

file_path=os.path.join("data","sample_data.csv")

df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path}")

