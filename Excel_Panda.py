from fileinput import filename
import pandas as pd
from requests import head

myFileName="./1.xlsx"

#打开excel文件
file=pd.read_excel(myFileName)

print(file.shape)
# 读取头两行
print(file.head(2))
print()

# 读取后两行
print(file.tail(2))

#保存excel文件

#index=False，去掉DataFrame的索引
file.to_excel("./2.xlsx",index=False)
