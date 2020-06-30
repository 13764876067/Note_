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
    
    python中,甚至类本身的定义都是可以修改的
    添加,修改类属性,
    添加,修改实例属性
    添加方法=>函数
    
    作用域问题:
    只有类才能修改创建类属性
    类可以影响实例,实例不能影响类
    
    不同实例的实例属性可以不同
    __dict__显示实例的所有属性
    
    self:指向自身,引用当前实例=>this
    
    方法:
    初始化方法=>构造器,实例创建时执行
    普通方法=>实例方法
    
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
    
    继承:对子类的实例化,会沿着继承链(A,B,C)从上到下,从左到右(子类继承括号的顺序)的顺序查找基类,然后按着相反的方式进行实例化
    #可以使用super来调用父类的被重载的方法
    #一定注意继承链的查找顺序
    
    #中间基类每一层都要调用super函数
    #不然继承链会在没有调用super函数的那一层断掉
    #对init亦是如此,对普通方法也是如此
    
    多态:(强类型(强检验参数类型),弱类型语言(不检验参数类型))
    python自身带有多态类型,即弱类型语言,
    
    封装:__
    私有化
    提到面向对象，那么-定有对被访问对象的访问权限控制相关的功能，如public, protected, private等。
    而这里是python比较特别的地方，python没 有提供相关的机制，python的作者 认为类的设计和使用者应该
    进行充分的沟通，而不是依赖这种语法设计来保证访问权限。
    
    但是Python里面还是提供了一个替代方案来实现私有成员。在python中， 以"__"双下划线开头的成员是私
    有成员，外部调用者不能直接访问，注意这里提了一个直接，事实上，想访问还是有办法的。
    class A:
        def __init__ (self):
            self.__var1 = 1
            self.__var2 = 2
    a=A()
    print(a._A__var1 )#可以突破限制访问
    
3.自定义对象类型(魔术方法 magic method)
    类和类型
    ##str:用户,repr:解释器
    __repr__ , __str__
    
        到这里，带双下划线的方法已经出现过很多次了，这里正式介绍一下。
        Python中，所有以“_” 双下划线包起来的方法，都统称为“Magic Method”，中文称魔术方法。
    同时还存在"__"双下划线开头的成员，又是另外的用途，待会儿单独介绍。
        Magic method存在于类中-般作为实例方法，其与特定的python内建函数或特定操作对应-般都有特
    定的用途。换句话说，python中有-批Magic Method,其名字和用途是已经确定了的，我们只需要根据
    自己的需要，实现这些MagicMethod即可，python的一些语法和内建函数会自动依赖这些MagicMethod
    来运行。已经介绍过的__init__就是比较常见的一个，与之对应的是__del__ 这两个函数分别用于实例
    的初始化和删除，也就是其他面向对象语言中的构造器和析构器。
        python中有比较完善的垃圾回收机制，所以很多时候不需要使用析构器。虽然很多文献指出这个垃圾回
    收机制的效率不高(甚 至有人指出，禁用垃圾回收能提高python的运行效率)。前面已经用过的len函数，依
    赖于__len__ , 而dict的key必须实现__hash__等。关于Magic Method,可以使用dir这个内建函数去
    查询需要模仿实现的类型，里面都有什么方法。
    
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

#在python中，甚至类本身的定义都是可以随时被修改的。
class Greeter3:
    #Constructor
    def __init__(self, name):
            self.name = name
#独立于类定义的一个函数定义
def greet(this, loud=False):
    if loud:
        print('HELLO, %s!' % this . name . upper())
    else:
        print( 'Hello, %s' % this. name )
Greeter3.greet = greet #函数的定义可以在运行的时候被替换
g = Greeter3('Greeter3')
g.greet()
g.greet(loud=True)

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

#这里做个有意思的小程序,对于这个自定的class,运行len会返回当前系统的unix timestamp
import datetime
class my_len:
    def __len__(self):
        return int(datetime.datetime.now().timestamp())
        #python里面的unixtimes tamp包含毫秒，但是len只能处理整数
print(len(my_len()))
#当然这里的实现其实很不好,因为这种方式很奇怪,返回的数据让人很困惑.

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

#yield 可做为一个list迭代器
class my_List(object):
    def __init__(self):
        self.l = [1, 2, 3, 4]
        self.l.reverse() # 这里用的pop,是从后面开始的
    def __iter__(self):
        return self
    def __next__ (self):
        if len(self.l) > 0:
            return self.l.pop( )
        else:
            raise StopIteration
it = my_List().__iter__()
# it = iter(my_ List()) #或者可以用magic method
print(it)
print(next(it))
print(it.__next__()) #也可以调用一个magic method, 效果是一样的。
print (next(it))
print(next(it))
print(next(it)) # 已经访问完毕了，继续访问则会报错。

#可以看到，这里的自定方式，实现的这个my_ List在特定情况下可以当作List使用，但是这种语法有些繁琐，
#因此python中专门门提供了generator生成器语法。
def my_list():
    for i in [1,2,3,4]:
        yield i
# generator看上去就像是一个 普通的函数，只不过把return替换成 J yield
#每次执行到yield的时候，函数会胡返回一个值，但是并不结束
#而是把中间状态都保存起来，只要后续还有数据就可以继续访问
l = my_list()
for i in l:
    print(i)
t = my_list().__iter__()
# it = iter(I) #或者可以用magic method
print(it)
print(next(it))
print(it.__next__()) #也可以调用一个magic method, 效果是一样的。
print(next(it))
print(next(it))
print(next(it)) # 已经访问完毕了，继续访问则会报错。

print('---------------------------------------------迭代器和生成器-----------------------------------------------------')