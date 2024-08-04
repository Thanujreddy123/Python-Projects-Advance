my_dict = {
    "student":["thanuj","reddy","lily"],
    "sscore":[56,568,90]
}
import pandas as pd
result=pd.DataFrame(my_dict)
for key,val in result.iterrows():
    print(val)
    #iterrows will iterate over the rows