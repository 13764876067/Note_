'''
matplot 可视化
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 引入出数据
idCrad = pd.read_csv("../sample/test1.csv", encoding ='gbk')
print(type(idCrad))
print(idCrad.dtypes)
print(idCrad)

plt.plot()
#plt.show()

#画图操作
plt.plot(idCrad["confidence"],idCrad["money"])
plt.yticks(rotation=45)
plt.xticks(rotation=45)
plt.xlabel("confidence")
plt.ylabel("money")
plt.title("confidence-money")
#plt.show()

#画多图操作
fig = plt.figure()
sf1 = fig.add_subplot(2,2,1)
sf2 = fig.add_subplot(2,2,4)

sf1.plot(idCrad["confidence"],idCrad["money"],c='red')
sf2.plot(idCrad["money"],idCrad["confidence"])

#plt.show()

# 一个图展示多条曲线
fig1 = plt.figure(figsize=(16,6))
colors=['red','blue','green','orange','black']
h = np.arange(10,100,10)
for i in range(5) :
    v = 100*i + np.random.randn(9,1) * 100
    label = str(i * 10)
    plt.plot(h,v,c=colors[i],label=label)
plt.legend(loc='best')
#plt.show()

# 其他图示
data = np.random.randn(2,100)
print(data)
print(data[0])
print(data[1])
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].hist(data[0])
axs[0, 1].scatter(data[0], data[1])
axs[1, 0].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])
plt.show()
