#coding:utf-8

'''

1. python中的函数基础部分

函数基础
    函数也是对象fun
    fun函数对象本身 ,fun()函数被调用

嵌套函数(闭包closure)与装饰器*

特殊函数*
    lambda
    map
    filter
    reduce

'''
from mpmath import factorial

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
    闭包closure:
        内层函数对外层函数非全局变量的引用，就叫做闭包函数。闭包会一直存在内存当中,不会因为函数执
    行结束而被释放。设想如下情景，我们需要个函数，这个函数可以记住自己被调用了多少次，该如何编写
    这个函数。当然，可以用全局变量来实现，也可以考虑用后面的class来实现，但是这两种方式都需要引入
    额外的东西。
    def fun_ gen(): #生成函数的函数
        count=0
        def fun(var):
            nonlocal count #声明，引用外部函数的变量，不加这个会报错
            print('got {}'.format(var))
            count += 1
            print( 'invoked {} times'.format (count))
        return fun
    
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
    
    #带参数的装饰器
    
3.特殊函数:(操作有序序列sequence)
    lambda
    map:返回 map object用list去run一下,map本身产生一个generator,用list得到它的结果
    filter
    reduce
    
    lam = lambda x : x+3
    map(lambda x:x+3,range(10))
    
    print(list(map(lambda x,y,z:x+y+z,[1,2,3],[4,5,6],[7,8,9])))
    print([x+y+z for x,y,z in zip([1,2,3],[4,5,6],[7,8,9])])
    
    print(list(filter(lambda x:x>3 ,[1,2,3,4])))
    print([i for i in [1,2,3,4] if i > 3])
    
    print(reduce(lambda x,y:x+y ,'abc','def')) => 'abcdef'
    
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
from functools import wraps, reduce


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

'''
有时候，仅仅能够在函数调用前后做一些操作还不够 ,我们还希望我们]的decorator可以接受一些参数， 表现
些不同的行为， 这种时候，上述的trace就做不到， 我们需要-个更复杂的decorator:
'''
def trace(tag='tag', flag=True):
    #这个就是我们要用的带参数的decorator
    print('got vars tag:[{}] flag:[{}]' .format(tag, flag))

    def decorator(fun) :
    #这个decorator其实跟刚才上面定义的那个不带参数的trace最外层是一样的
        if flag:
            print('will trace:[{}]'.format(fun))
        else:
            print('will not trace:[{}]'.format(fun))

        def wrapper(*args, **kwargs ):
            '''
            这个是decorator的返回值，一般是个函数
            事实上，这个返回的函数，会被用来代替被decorate的函数被调用

            因此，这个函数需要能处理任何参数输入，因为很多时候，-个decorator并不知道，
            要被decorate的函数是什么样子，接收什么样的参数，而我们]前面见过的*参数就能
            很好解决这个问题
            :param args:
            :param kwargs:
            :return:
            '''
            print('inside trace the tag is:[{}]'.format(tag))
            if flag:
                start = time.time()

            var = fun(*args, **kwargs)
            # 在这个函数内部调用被decorate的函数
            #可以看出来，这里的fun是外面传进来的，很典型的闭包

            if flag:
                period = time.time() - start
                print('used:[{}]'.format(period))

            return var  # 不要忘了处理fun的返回值。

        return wrapper

    return decorator
@trace(tag='trace_2')
def compute(num=128):
    factorial(num)
compute(1024)

@trace(tag='trace_2',flag=False)
def compute(num=128):
    factorial(num)
compute(1024)

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

print(reduce(lambda x,y :x+y ,'abc','def'))

print('---------------------------------------------特殊函数 部分-----------------------------------------------------')