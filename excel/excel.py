import pandas as pd
import os #用到的一个新库
import re


name_list=os.listdir("./")
url="./"
data=[] 
for x in range(len(name_list)):
    df=pd.read_excel(url+name_list[x])#循环导入多个excel文件
    data.append(df)#将每个excel写入到data变量中
data=pd.concat(data)#合并data变量，转化成Dataframe
data.to_excel("./sum/"+'sum.xlsx',index=False)#输出合并后的excel





