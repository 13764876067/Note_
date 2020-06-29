#coding:utf-8

'''
1. python中的函数基础笔记
    函数基础

'''

'''
1.函数基础
    def function _name(x,y,z):
        do something
        return object

    函数调用
    按位置提供参数
    指明参数名称
    设置参数默认值
    参数数集(不定参数): * , **的使用
    
    返回值
    返回一个值
    返回多个值
'''

print('---------------------------------------------函数基础  部分-----------------------------------------------------')

def add(x,y):
    return x + y

def add1(x=2,y=3):
    return x + y, x * y

print(add(2,4),add('a','dbc'),add1(),add1(y=3),add1(x=3),add1(4))

print(add(2,4),add('a','dbc'))

def convert(s):
    lst = [i.upper() if i == i.lower() else i.lower() for i in s]
    return "".join(lst)

print(convert('Python'),convert('Hello'))

def par(x,*args):
    print(x,args)
def par1(x,**kwargs):
    print(x,kwargs)

par(1,2,3,4,5)
par1(1,b=3,c=4,d=5)

print('---------------------------------------------函数基础  部分-----------------------------------------------------')