'''
pandas 主要对数据集进行处理
'''

import pandas as pd
import numpy as np

#读取文件

idCrad = pd.read_csv("../sample/test1.csv",encoding = 'gbk')
print(type(idCrad))
print(idCrad.dtypes)

print(idCrad.head())

print(idCrad.head(3))

print(idCrad.tail(3))

print(idCrad.columns)

print(idCrad.shape)

print(idCrad.loc[2])

print(idCrad[3:6])

print(idCrad[["name","confidence"]])

print(idCrad["confidence"] / 10)

cmoney = idCrad["money"] / idCrad["confidence"]
idCrad["cmoney"] = cmoney
print(idCrad)

print(idCrad["confidence"].max())
print(idCrad["confidence"].min())
print(idCrad["confidence"].mean())

idCrad.sort_values("money",inplace=True,ascending=True)
print(idCrad)

# 空值处理
idCrad0 = pd.read_csv("../sample/test2.csv",encoding = 'gbk')
print(type(idCrad0))
print(idCrad0.dtypes)
print(idCrad0)

print(pd.isnull(idCrad0["confidence"]))

print(sum(idCrad0["confidence"]))

isnan = pd.isnull(idCrad0["confidence"])
idCrad1 = idCrad0["confidence"][isnan == False]
print(idCrad1)

print(sum(idCrad0["confidence"][isnan == False]))

# 分组 sex
print(idCrad0.pivot_table(index="sex",values="money",aggfunc=np.sum))

