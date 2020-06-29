#coding:utf-8

'''

1. python中的函数基础部分

函数基础
    函数也是对象fun
    fun函数对象本身 ,fun()函数被调用

嵌套函数与装饰器*

特殊函数*
    lambda
    map
    filter

'''

'''
1.函数基础:
    def function _name(x,y,z):
        do something
        return object

    函数调用(参数引用类型,复制)
    按位置提供参数
    指明参数名称
    设置参数默认值
    参数数集(不定参数): * , **的使用
    
    返回值
    返回一个值
    返回多个值
    
    作用域:global局部变量,nonlocal非局部的
    局部变量,全局变量
    
2.嵌套函数和装饰器:
    def opt_seq(func,seq):
        return [func(i) for i in seq]
    opt_seq(abs,{-1,-2,3})
    opt_seq(str,[1,2,3])
    
    def weight(g):
        def cal_mg(m):
            return m*g
        return cal_mg
    w=weight(10)
    print(w(2))
    print(w(30))
    
    装饰器:嵌套函数的基础
    
    def p_deco(func):
        def wrapper(name):
            return "<p>{0}<p>".format(func(name))
        return wrapper

    def d_deco(func):
        def wrapper(name):
            return "<d>{0}<d>".format(func(name))
        return wrapper

    def book0(name):
        return 'the name of my book is {0}'.format(name)

    print(p_deco(book0)("python"))

    #装饰器函数,多层装饰器
    @d_deco
    @p_deco
    def book(name):
        return 'the name of my book is {0}'.format(name)
    py_book = book("python")
    print(py_book)
    
3.特殊函数:
    lambda
    map
    filter
    
    lam = lambda x : x+3
    map(lambda x:x+3,range(10))
    
    print([x+y+z for x,y,z in zip([1,2,3],[4,5,6],[7,8,9])])
    print(list(map(lambda x,y,z:x+y+z,[1,2,3],[4,5,6],[7,8,9])))
    
    print(list(filter(lambda x: x>3 ,[1,2,3,4])))
    print([i for i in [1,2,3,4] if i > 3])
    
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

print('---------------------------------------------嵌套装饰 部分-----------------------------------------------------')

def foo(a):
    a.append(99)
    return a
ls=[]
print(foo(ls),ls)

def fun(fun1):
    return fun1()
def opt_seq(func,seq):
    return [func(i) for i in seq]
opt_seq(abs,{-1,-2,3})
opt_seq(str,[1,2,3])

def fun1():
    def bar():
        print('in')
    return bar
print(fun1())
fun1()()


def weight(g):
    def cal_mg(m):
        return m*g
    return cal_mg
w=weight(10)
print(w(2))
print(w(30))

def p_deco(func):
    def wrapper(name):
        return "<p>{0}<p>".format(func(name))
    return wrapper
def d_deco(func):
    def wrapper(name):
        return "<d>{0}<d>".format(func(name))
    return wrapper
def book0(name):
    return 'the name of my book is {0}'.format(name)
print(p_deco(book0)("python"))
#装饰器函数,多层装饰器
@d_deco
@p_deco
def book(name):
    return 'the name of my book is {0}'.format(name)
py_book = book("python")
print(py_book)

import time
from functools import wraps
def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end - start)
    return wrapper
@timethis
def countdown(n):
    while n > 0:
        n -= 1
countdown(10000000)
#countdown(2000000000)

print('---------------------------------------------嵌套装饰 部分-----------------------------------------------------')

print('---------------------------------------------特殊函数 部分-----------------------------------------------------')

lam = lambda x : x+3
print(lam(3))

m = map(lambda x:x+3,range(10))
print(list(m))

print([x+y+z for x,y,z in zip([1,2,3],[4,5,6],[7,8,9])])
print(list(map(lambda x,y,z:x+y+z,[1,2,3],[4,5,6],[7,8,9])))

print(list(filter(lambda x: x>3 ,[1,2,3,4])))
print([i for i in [1,2,3,4] if i > 3])

print('---------------------------------------------特殊函数 部分-----------------------------------------------------')