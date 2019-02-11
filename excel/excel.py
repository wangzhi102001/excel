import pandas as pd
import os #用到的一个新库
import re

a = input('''
请将需要合并的excel文件放到data文件夹，并让此程序与data文件处于同一目录下。
开始合并Y/N？？
''')
if a.lower() =="y":    
    url="./data/"
    name_list=os.listdir(url)
    data=[] 
    for x in range(len(name_list)):
        df=pd.read_excel(url+name_list[x],dtype=object)#循环导入多个excel文件
        data.append(df)#将每个excel写入到data变量中
        print("正在合并第%s个文件" % str(x+1))
    data=pd.concat(data, axis = 0, ignore_index = True,sort= False)#合并data变量，转化成Dataframe
    data.to_excel('sum.xlsx',index=False)#输出合并后的excel
    print("合并完成，请查看sum.xlsx文件")
    input("按任意键关闭窗口")
else:
    print("程序退出")
    input("按任意键关闭窗口")





