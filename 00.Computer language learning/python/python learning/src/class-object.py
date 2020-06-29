#coding:utf-8

'''

1. python中的类与对象部分

面向对象 OOP <=> 面向过程

类
    静态属性
    self
    特殊方法(初始方法)
    普通方法(实例方法)

对象
    动态属性
    普通方法(实例方法)

继承,多态,封装

自定义对象类型*

控制对象属性*

迭代器和生成器*

'''

'''

面向对象

1.类class,对象object
    创建类 class Foo()
    创建对象:实例化 SuperMan('guojing')
    
    属性:
    类属性,=>静态属性
    实例属性,=>动态属性
    
    添加,修改类属性,
    添加,修改实例属性
    
    作用域问题:
    只有类才能修改创建类属性
    类可以影响实例,实例不能影响类
    
    不同实例的实例属性可以不同
    __dict__显示实例的所有属性
    
    self:指向自身,引用当前实例=>this
    
    方法:
    初始化方法=>构造器,实例创建时执行
    普通方法
    
    装饰符
    @classmethod :cls表示类本身
    @staticmethod :静态方法不与实例绑定
    
2.面向对象三大特性
    继承:
    class 子类(父类,父类):
    
    子类对父类的重写:(子类覆盖父类的方法)=>初始化方法,普通方法
    
    初始化方法的嵌套(子类调用父类)调用:=>(即this,super关键字)
    
    单继承:可以用super()
    多继承:__mro__
    
    多态:(强类型(强检验参数类型),弱类型语言(不检验参数类型))
    python自身带有多态类型,即弱类型语言,
    
    封装:__
    私有化
    
3.自定义对象类型
    类和类型
    ##str:用户,repr:解释器
    __repr__ , __str__
    
4.控制属性访问
    1.优化内存: __slots__
        __slots__ = ('name','age') => 不能增加和改变这个类的属性,只读
    2.特殊方法: __getattr__ , __setattr__ 
        设置和获取属性
        
5.迭代器和生成器:优化内存
    迭代器:
    hasattr(list,"__iter__"):是否可迭代
    iter():创建迭代器
    __next__()
    
    自定义迭代器类型:
    
    生成器:generator,也可迭代
    yield:关键字 挂起
    yield n :返回n,并挂起暂停
    print([x ** 2 for x in range(10)])
    print((x ** 2 for x in range(10)).__next__):生成器对象
    
6. Fraction 模块分数对象
    from fraction import Fraction
    Fraction(1,6) => 1/6
    Fraction(1,6) + Fraction(1,6) => 1/6 + 1/6
    + - * /
    
    itertools模块 迭代器工具
    帮助构造迭代器对象
    
'''

print('---------------------------------------------类和对象 部分-----------------------------------------------------')

class SuperMan:
    ''' A class of Superman'''
    lang=1
    def __init__(self,name):
        self.name = name
        self.gender = 1
        self.single = False

    def nine_negative_kungfu(self):
        return " ya! you have to die!"
guojing = SuperMan('guojing')
print(guojing.gender,guojing.name,guojing.nine_negative_kungfu())

class Student:
    ''' A class of Student'''
    def __init__(self,name):
        self.name = name
    def do_work(self,time):
        return True if time < 3 else False

class Teacher:
    ''' A class of Teacher'''
    def __init__(self,name):
        self.name = name
    def evaluate(self,bl):
        return "good!" if bl else "bad!"
print(Teacher("jion").evaluate(Student("luck").do_work(6)))
print(Teacher("John").__dict__)

class Foo:
    lang = 'python'
    def method(self,x):
        return x*x
f = Foo()
print(Foo.lang,f.lang,f.method(2),Foo.method(f,2))
Foo.group = 'a'
print(Foo.group,f.group)
f.name = "lee"
print(f.name,Foo.__name__)

import datetime
from dateutil import rrule
class BeDate:
    def __init__(self,s_time,e_time):
        self.s_time = datetime.datetime.strptime(s_time,"%Y, %m, %d")
        self.e_time = datetime.datetime.strptime(e_time,"%Y, %m, %d")
    def days(self):
        return (self.e_time - self.s_time).days  if (self.e_time - self.s_time).days > 0 else False
    def weeks(self):
        return rrule.rrule(rrule.WEEKLY,dtstart=self.s_time,until=self.e_time).count()
print(BeDate("2019, 5, 1","2019, 11, 25").days(),BeDate("2019, 5, 1","2019, 11, 25").weeks())

class Bar:
    @classmethod
    def method(cls,x):
        print(cls)
    @staticmethod
    def meth(x):
        print(x*x)
print(Bar().method(2),Bar.method(4),Bar.meth(4))

class Date(object):
    def __init__(self,y=0,m=0,d=0):
        self.y=y
        self.m=m
        self.d=d
    @classmethod
    def from_string(cls,date_as_string):
        return cls(map(int,date_as_string.split('-')))
    @staticmethod
    def is_date_vaid(date_as_string):
        return list(map(int,date_as_string.split('-')))[0] <=2038 and list(map(int,date_as_string.split('-')))[1] <= 13 and list(map(int,date_as_string.split('-')))[2] <= 31
print(Date.from_string('2019-11-11').is_date_vaid('2019-11-11'),Date.is_date_vaid("2039-11-11"))

print('---------------------------------------------类和对象 部分-----------------------------------------------------')

print('---------------------------------------------对象的三大特性-----------------------------------------------------')

#单继承:
class P:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("food!")
class C(P):
    pass
print(C('a').name)
class E(P):
    def __init__(self,name,age):
        self.age = age
        super().__init__(name) # P.__init__(self,name)
print(E('name','age').name,E('name','age').age)

#多继承
class K1:
    def foo(self):
        print('k1-foo')
class K2:
    def foo(self):
        print('k2-foo')
class J1(K1,K2):
    pass
class J2(K1,K2):
   def bar(self):
       print('J2-bar')
class C(J1,J2):
    pass
print(C.__mro__)
m = C()
m.foo()
m.bar()

#多态
def add(x,y):
    return x+y
print(add('abc','cdb'),add(1,2))

#封装
class A:
    def __init__(self):
        self.name = 'name'
        self.__gourp = 'group'
    def eat(self):
        return self.__gourp
    def __eat(self):
        return self.name

print('---------------------------------------------对象的三大特性-----------------------------------------------------')

print('---------------------------------------------自定义对象类型-----------------------------------------------------')

class Fraction:
    def __init__(self,number,denom=1):
        self.number = number
        self.denom = denom
    def __str__(self): ##str:用户,repr:解释器
        return str(self.number) + "/" + str(self.denom)
    __repr__ = __str__
print(Fraction(2,3))
Fraction(1,3)

print('---------------------------------------------自定义对象类型-----------------------------------------------------')

print('---------------------------------------------控制的属性访问-----------------------------------------------------')

class Fo:
    __slots__ = ('name','age')

class B:
    def __getattr__(self, i):
        print('get')
    def __setattr__(self, i, value):
        print('set')
        self.__dict__[i] = value
b = B()
print(b.x)
b.x = '1'
print(b.x)
'''
get
None
set
1
'''

print('---------------------------------------------控制属性的访问-----------------------------------------------------')

print('---------------------------------------------迭代器和生成器-----------------------------------------------------')

print(hasattr(list,"__iter__"))
iter_ls = iter([1,2,3,4,5])
print(iter_ls.__next__())

class Myrange:
    def __init__(self,n):
        self.i = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return i
        else :
            raise StopIteration()
print(list(range(7)))
print([i for i in Myrange(7)])

class Fibs:
    def __init__(self,max):
        self.a = 0
        self.b = 1
        self.max = max

    def __iter__(self):
        return self
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a,self.b = self.b,self.a + self.b
        return fib
fb = Fibs(10000)
print([fb.__next__() for i in range(10)])

def g():
    yield 0
    yield 1
    yield 2
ge = g()

def y_yield(n):
    print('strat')
    while n > 0 :
        print("before yield")
        yield n
        n -= 1
        print("after yield")

yy = y_yield(3)
print(yy.__next__())
print(yy.__next__())
print(yy.__next__())

def fib():
    prev,curr = 0,1
    while True :
        yield prev
        prev,curr = curr,prev+curr

import itertools
print(list(itertools.islice(fib(), 10)))

print([x ** 2 for x in range(10)])
print((x ** 2 for x in range(10)))

print('---------------------------------------------迭代器和生成器-----------------------------------------------------')