# testBasis conda pakage
# python note
'''
多行注释
'''

import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn as sn

'''
输入，输出
'''
print("testBasis np, pd, mpl, sn is OK !!")

print("np","pd","mpl","sn")

print(300)

print(200+300)

print("200+300",200+300)

#name=input()
#print(name)

#id=input("id:")
#print("id:",id)

'''
数据类型和变量
'''

print(1,-200,0,1.23,-0.02,"ai",'ai')

print('i\'m tensorflow')

#list

ls=[1,2,3]
print(ls)
print(len(ls))

print(ls[1])
print(ls[-1])

ls.append(4)
print(ls)
ls.insert(0,0)
print(ls)

ls.pop()
print(ls)

ls[0]=-1
print(ls)

#tuple 不能修改

tup=(1,2,3)
print(tup)

# 条件判断 if

price = 100
if price <= 80 :
    print("buy")
else :
    print("don't buy")

if price <= 80 :
    print("buy")
elif price <= 50 :
    print("two buy")
else :
    print("don't buy")

# 循环结构 for

lst=[0,1,2,3,4]

for x in lst :
    print(x)

#range()
for x in range(10) :
    print(x)
print(list(range(101)))

sum = 0
for x in list(range(101)) :
    sum = sum + x
print(sum)

# while

sum1 = 0
n = 0
while   n < 101 :
    sum1 = sum1 + n
    n = n + 1
print(sum1)


#break continue

sum2 = 0
for x in list(range(101)) :
    if x > 50 :
        break
    sum2 = sum2 + x
print(sum2)

sum3 = 0
for x in list(range(101)) :
    if x % 2 == 1  :
        continue
    sum3 = sum3 + x
print(sum3)

#dict key-value

d={'1':'a','2':'b'}
print(d['1'])
print(d.get('2'))
d.pop('2')
print(d)

#set 不能重复

s = set([1,2,3])
print(s)

s.add(4)
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)

s.add('a')
print(s)



#内置函数

print(abs(-100))
print(max(-1,2,3))
print(min(-1,-2,3))
print(int('123'))
#print(int('abc'))
print(int(12.23))
print(float('123.23'))
print(str(123))
print(bool(0))
print(bool(1))
print(bool(2))


#自定义函数

def my_fun(x) :
    if x >= 0 :
        return x
    else :
        return -x
print(my_fun(100))
print(my_fun(-100))

def my_fun1() :
    print("None...")
    return
print(my_fun1())

def return_more_result() :
    a=300
    b='abc'
    return a,b
x,y=return_more_result()
print(x,y)

# 切片

print(ls)

print(ls[0:2])
print(ls[:2])
print(ls[1:3])
print(ls[:])

# 模块的引用

#import nump as np

data=[1,2,3,4]
dt=np.array(data)
print(dt)