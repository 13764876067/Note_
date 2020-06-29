#coding:utf-8

'''
面向对象编程<-->面向过程编程
分析
面向过程{函数}
对象{属性,方法}

1.python 内置对象部分

内置对象类型
    整数(int),浮点数(float)
    字符串:(ascii)
    列表
    元组
    字典
    集合
    布尔

内置函数

四则运算与逻辑运算

***变量与对象

'''

'''
built-in_functions:内置函数(函数名称对pyhton来说也是对象):

1.整型和浮点型:
    help():返回帮助文档
    type():打印类型
    int(),float():类型转换(整数,浮点数)
    id():打印对象的地址,判断是否相等
    round():四舍五入
    + - * / % // divmod(x,y):四则运算
    e:科学计数法

    math模块
    dir():返回属性
    pi:π(3.141592653)
    pow(2,3): 2的3次方 :x**y

    溢出问题:float的溢出问题
    decimal 模块
    decimal.Decimal() 

    数字计算中的异常

2.字符和字符串:
    ord():返回ASCII码
    bin():返回二进制
    chr():转换
    sys.getdefaultencoding()
    int():字符转换类型
    \ :转移字符
    有序排列:序列
    + * :字符串操作
    len():求长度
    in:是否存在,is:是否为同一个对象
    
    索引和切片:chr[::]  -> chr[0],chr[-1],chr[0:2]
    print(),input():输出,输入
    
    字符串属性和方法:
    islower(),upper(),lower():大小写翻转
    isalpha():是否字符
    index():返回子集的索引
    join():多个字符串的连接
    split():切分字符串
    format():格式化输出 "a {0:10} and {1:>15}".format('a','b')
    
    字符编码集:Unicode,utf-8
    
3.列表和元组: 序列,容器
    列表:
    ls = []  ls = list():定义 
    ls[0] = 'a' :列表修改
    + * :字符串操作
    索引和切片:ls[::]  -> ls[0],ls[-1],ls[0:2]  ls[::-1]
    
    方法:dir(list)
    append():追加,无返回值
    insert():指定位置插入
    pop():弹出(删除)
    remove():删除指定位置
    clear():清空
    sort():排序(同种类型)
    reverse():反序
    list():将字符串转为列表
    str():将列表转换为字符串
    
    与字符串比较:
    都是序列
    列表是容器可变,字符串不可变
    
    元组:不可修改,元组运算速度快,容器,序列对象
    t=() tuple()  t = ('a',) 元组 与  t = ('a') 字符串
    + * :字符串操作
    t[::] 索引和切片:t[::]  -> t[0],t[-1],t[0:2]  t[::-1]
    list(t),tuple(ls):互相转换
    
4.字典和集合:不是序列,可变对象
    字典:dict(k,v), k为不可变对象
    dict={},dict(a=1,b=2),d = {"a":1,"b":2}
    dict["key"] = vaule
    d = dict([('a',1),('b',2),('c',4)])
    d = dict({'a':1,'b':2})
    
    方法:
    get():返回key的vaule
    setdefault():设置值,插入
    update():增加键值对
    print(dic.update([('a',4),('d',5)]))
    print(dic.update({'e':6})
    
    del dic['a']:特殊的删除写法, in 是否存在
    pop():删除某个值
    poopitem():弹出最后一个值
    
    字典和列表:字典不是序列,容器类对象,可变对象,python3.6开始字典key也有顺序(创建时的顺序)
    
    集合:set,无序,(不能用可变对象作为set里的元素)
    可变集合,
    set([1,2,3,4]),{}
    add():添加元素
    pop():弹出元素
    remove():删除元素没有时报错
    diccard():删除元素没有时不报错
    
    不可变集合,一旦创建就不可变
    frozenset([]),{}
    
    copy():a shallow copy of D,浅拷贝
    import copy => copy.deepcopy(),深拷贝
    
    集合运算: 
    issubset():子集
    | union ,& intersection, - difference,并交差集
    
    哈希表,哈希code
    
5.布尔类型bool,值只有True和False
    四则运算:True:1,False:0 (默认)    
    True + 1
    bool():定义
    任何空对象为False,任何不为空对象为True
    检查对象是否为空,
    
    比较运算: > , < , == , != , >= , <=
    返回值 True,False
    逻辑运算: and , or , not 
    返回值 左边或者右边的对象
    
5.import用法
    import module
    import module as new_name 
    from muodule import function
    from muodule import function as new_name
    form module import *

'''

print('---------------------------------------------整数,浮点数部分-----------------------------------------------------')
#1. 变量a,对象3,变量不能单独定义.必须赋值
a = 3
b = 4
print(a,b)
a,b = b,a #调换a,b
print(a,b)

my_book = "python test!!!"
print(my_book)

print(type(2))
print(type(3.14))

print(int(3.14))
print(float(3))

print(id(a))
print(id(b))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(divmod(a,b))

print(help(id))

print(0.1 + 0.2) # 浮点数的计算
print(round(0.1+0.2,3))
print(round(1.23456,3))

print(2e2,2E2)

import math

print(help(dir))
print(dir(math))

print(math.pi)
print(math.pow(2,3))


#计f1和f2的合力,物理问题
f1 = 20
f2 = 10
alpha = math.pi / 3

x_force = f1 + f2 * math.sin(alpha)  # 20 + 10 * sin(pi / 3) = 20 + 10 * 根号3/2  = 20 + 5倍根3
y_force = f2 * math.cos(alpha) # 10 * 1/2 = 5

force = math.sqrt(x_force * x_force + y_force ** 2)
print('the result is: ',round(force,2),'N')

import decimal
print(decimal.Decimal('0.1') + decimal.Decimal('0.2'))

print('---------------------------------------------整数,浮点数部分-----------------------------------------------------')


print('---------------------------------------------字符,字符串部分-----------------------------------------------------')

print(ord('a'))
print(bin(97))
import sys
print(sys.getdefaultencoding())

st = "python"
chr = 'book'
print(type(st),type(chr),int('123'))

print(st + chr)
print(chr * 3)
print(len(chr))
print('b' in chr)

print(len(chr))
print(chr[0],chr[-1],chr[1])
print(chr[0:2])
print(dir(st))
print(help(st.index))

print(st.index('y'))
print(st.split("y"))
print("-".join(st))
print("a {0:10} and {1:>15}".format('a','b'))

print('---------------------------------------------字符,字符串部分-----------------------------------------------------')

print('---------------------------------------------列表,元组 部分-----------------------------------------------------')

ls=[]
lst = list()
s = str()

ls = [2,3.14,True,'a',"python",[]]
print(ls)
print(ls[1])
print(ls[0:2])
ls[0] = 0
print(ls)

print(dir(list))
ls.append('a')
ls.insert(2,'b')
print(ls)

t = (1,1.2,'a',"py")
print(type([1,]),type([1]))
print(type(t),t)
print(dir(t))

print('---------------------------------------------列表,元组 部分-----------------------------------------------------')

print('---------------------------------------------字典,集合 部分-----------------------------------------------------')

print(type({}))
d = {"a":1,"b":2}
di = dict(a=1,b=2)
d = dict([('a',1),('b',2),('c',4)])
d = dict({'a':1,'b':2})

print(d,di,d["a"])
dic = dict([('a',1),('b',2)])
print(type(dic))
print(dic["a"],dic.get("c",'n'))
print(dic.setdefault('c',3))
print(dic.update([('a',4),('d',5)]))
print(dic.update({'e':6}))
print(dic)

del dic['a']
print(dic)

dic.pop("b")
print(dic)

se = set([1,2,3,4])
print(se,type(se))

#se1 = set({'pyton',[1,2,3]})
se1 = set({'a','b'})

print(help(dict.copy))

print('---------------------------------------------字典,集合 部分-----------------------------------------------------')

print('---------------------------------------------布尔类型  部分-----------------------------------------------------')

bo = True
print(bo + 1)
print(bool(" "))
print(bool())

print('---------------------------------------------布尔类型  部分-----------------------------------------------------')
