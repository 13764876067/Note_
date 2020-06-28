'''
numpy 主要进行矩阵的相关计算
'''

import numpy as np

#print(help(np.array))

npArr = np.array([0,2,3,4],dtype=float)
print(npArr)
print(type(npArr))
print(npArr.dtype)
print(npArr.shape)

npArr1 = np.array([0,2,3,4.0])
print(npArr1)
print(type(npArr1))
print(npArr1.dtype)
print(npArr1.shape)

#二维，多维方式
npArr0 = np.array([[0,1,2],
                   [3,4,5],
                   [6,7,8],
                   [9,10,11]])
print(npArr0)
print(type(npArr0))
print(npArr0.dtype)
print(npArr0.shape)

#从文件读取数据 genfromtxt
testsample = np.genfromtxt("../sample/testsample.txt",delimiter=',',dtype=str)
print(testsample)
print(type(testsample))
print(testsample.dtype)
print(testsample.shape)

# index从0开始
print(testsample[0,2])
print(testsample[1,2])

# 切片的用法
print(testsample[0:1])
print('------------------------------------')
print(testsample[:,2])
print('------------------------------------')
print(testsample[:,0:2])
print('------------------------------------')
print(testsample[0:1,0:1])
print('------------------------------------*')
print(testsample[1:])
print('------------------------------------*')

#值比较
'''
npArr0 = np.array([[0,1,2],
                   [3,4,5],
                   [6,7,8],
                   [9,10,11]])
'''
#行切片
print(npArr == 2)
print('------------------------------------1')
print(npArr0[1])
print('------------------------------------2')
print(npArr0[1:])
print('------------------------------------3')
print(npArr0[1:3])
print('------------------------------------4')
#列切片
print(npArr0[:,1])
print('------------------------------------5')
print(npArr0[:,1:])
print('------------------------------------6')
print(npArr0[:,0:2])
print('------------------------------------7')

#行和列
print(npArr0[2:,1])
print('------------------------------------8')
print(npArr0[1:,1:])
print('------------------------------------9')
print(npArr0[0:2:,0:2])
print('------------------------------------10')

#
print(npArr0[npArr0[:,2] == 5,:])
print(npArr0[npArr0[:,1] == 7,:])
print('------------------------------------11')
#print(npArr0[:,npArr0[:,2] == 5])  erro: boolean index did not match indexed array along dimension
print(npArr0[npArr0[:,2] == 5,:])

#逻辑判断 & |
print((npArr0 % 2 == 0) & (npArr0 % 3 == 0))
print('------------------------------------12')
print((npArr0 == 2) | (npArr0 == 3))
print('------------------------------------13')

print((npArr0 == 2) | (npArr0 == 3))
print('------------------------------------14')

npArr0[(npArr0 == 2) | (npArr0 == 3)] = 10
print(npArr0)
print('------------------------------------15')

#类型转换
print(npArr0.dtype)
print(npArr0.shape)
print('------------------------------------16')
npArr0 = npArr0.astype(float)
print(npArr0.dtype)
print(npArr0)
print('------------------------------------17')

#求 max min
npArr0 = npArr0.astype(int)
print(npArr0)
print(npArr0.max())
print(npArr0.min())
print(npArr0.mean())
print('------------------------------------18')

#求总和,以及按照维度求和
print(npArr0.sum())
print(npArr0.sum(axis=1)) #按行求和
print(npArr0.sum(axis=0)) #按列求和
print('------------------------------------19')

print(np.arange(10))
print(np.arange(0,20,4))
print('------------------------------------20')

# 矩阵变换
np1 = np.arange(40).reshape(4,5,2)
print(np1)
print(np1.shape)
print('------------------------------------21')

print(np1.ndim)
print(np1.size)
print('------------------------------------22')

#矩阵初始化

print(np.zeros((3,5)))
print(np.ones((3,5,3),dtype=np.int64))
print('------------------------------------23')

from numpy import random as rd
print(rd.random((2,3)))
print('------------------------------------24')

from numpy import pi
print(np.linspace(1,pi,50))
print('------------------------------------25')

#矩阵加减法

matrix1 = np.array([
    [0,1,2],
    [3,4,5]]
)
matrix2 = np.array([
    [6, 7, 8],
    [9, 10, 11]]
)

print(matrix1 + matrix2)
print('------------------------------------26')
print(matrix2 - matrix1)
print('------------------------------------27')

#矩阵乘法
matrix2 = matrix2.reshape(3,2)
print(matrix1)
print(matrix2)
print(np.dot(matrix1,matrix2))
print('------------------------------------28')

#矩阵的其他操作

matrix3 = np.floor(np.random.random((3,4)) * 10)
print(matrix3)
print(matrix3.ravel())
matrix3.shape=(2,-1)
print(matrix3)
print(matrix3.T)
print('------------------------------------29')

# e
print(np.exp((1)))
print(np.exp((np.arange(3))))
print(np.sqrt(4))
print('------------------------------------30')

# 拼接和切分操作
matrix4 = np.floor(np.random.random((2,4)) * 10)
print(matrix4)

matrix5 = np.floor(np.random.random((2,4)) * 10)
print(matrix5)
print('------------------------------------31')

print(np.hstack((matrix4,matrix5)))
print(np.vstack((matrix4,matrix5)))

print(np.hsplit(matrix4,2))
print(np.vsplit(matrix4,2))
print('------------------------------------32')

#求维度中的最大元素的位置
matrix6 = np.floor(np.random.random((2,4)) * 10)
print(matrix6)
print(matrix6.argmax(axis = 1))
print(matrix6.argmax(axis = 0))
print('------------------------------------33')

#矩阵的扩展
print(np.tile(npArr0,(2,3)))

#矩阵排序
print(npArr0)
print(np.sort(npArr0,axis=1))
print(np.argsort(npArr0,axis=1))
print('------------------------------------34')

#特征值分解
matrix7 = np.array([
    [2,3],
    [2,1]
])
a,b=np.linalg.eig(matrix7)
print(a,b)
print('------------------------------------35')