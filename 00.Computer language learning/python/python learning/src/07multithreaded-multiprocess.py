#coding:utf-8

'''

1.python 中的多线程与多进程操作部分

GIL

多线程操作

多进程操作

'''

'''

1.GIL,多线程,多进程的关系
        在介绍python的多线程多进程之前，首先来了解一下python里面最大的一个坑，也是最为其他语言和框架的使
    用者诟病的一点:GIL(global interpreter lock):
        python是一个语言的规范，目前广泛使用的的是一种叫做CPython的实现。 CPython实现的python解释器里
    面有个全局解释器锁(Global Interpreter Lock) GIL, 这个东西本身并不是python规范里面的东西，所以罪
    魁祸首不是python,而是CPython。 CPython的市场最大， 所以一般提python就是CPython,本文未加区别。其
    他一些实现如JPython (跑在JVM上)或者lronPython (跑在 .Net上)没有GIL问题。
        目前CPU都是多核的，为了利用多核，就出现了多线程技术。而多线程技术处在同一个进程中，数据为所有线程共
    有，所以数据同步是一个非常严峻的问题。 python中为了简化这个问题，引入了一个非常navie的方案，就是全局加
    锁，interpreter在执行代码的时候，同-时刻，只执行一个线程的代码，并且规定个线程的代码在执行一段时间后，
    必须释放interpreter, 切换到另一个线程执行。所以很多时候可以认为python是单线程执行的。同时由于获取释放
    锁的开销，导致了python的多线程性能在CPU密集的任务中表现极其糟糕。
        当然只是在CPU密集的任务上，I0密集的任务由于I0操作不涉及线程切换，所以使用多线程是可以有效的提高效率
    的。同时,python的多进程是开启了多个进程，每个进程都有一个python的interpreter,所以能够充分的利用多核
    提升CPU密集型任务的运算性能.
        GIL是一个历史遗留问题，很多库都有意无意的利用了GIL,大大简化了多线程代码的设计。库太多导致GIL暂时没
    有很好的解决方案。需要注意的是，GIL问题只存在与于python的解释器中，很多操作，如opencv的图片处理，是用
    C/C++写的，不在GIL的控制范围内，所以没有性能问题。
        Tensorflow/pyTorch/mxnet等深度学习框架,其compute engine也是C++实现的,本身不再
    python的程序空间内,所以也没有GIL的性能问题.
        python自带的multiprocessing库提供了很好的对多线程/多进程的支持，而且简单易用.
    尝试计算.

'''

print('---------------------------------------------多线程多进程操作-----------------------------------------------------')

def count(num) :
#计算从0到nu的所有整数的和
    var = 0
    for i in range(num + 1):
        var=var+i
    return var

from multiprocessing.dummy import Pool as ThreadPool # 多线程执行，dummy是伪多进程
#多线程版
p = ThreadPool() #创建个线程池
results = p.map(count, range(10)) # 把任务放入线程池
p.close() #关闭线程池
p.join() #等待线程池的所有任务完成
print(results) # 取得结果


#把线程换成进程就是下面的操作
from multiprocessing import Pool as ProcessPool # 多进程执行
p = ProcessPool()
results = p.map(count, range(10))
p.close()
p.join()
print(results)

#自定义线程
from threading import Thread
import time
class myThread( Thread):
    def run(self): #重载这一个函数，把所有的任务逻辑都放在这个函数里面
        for i in range(10):
            print('child process is working' )
            time. sleep(1)
my_thread = myThread()
my_thread.start() # 不是调用run,而是调用这个start去启动一个线程
print(my_thread.is__alive())
my_thread.join()
#等待子线程退出，如果没有这一句，那么主线程退出会直接干掉子线程
#不过我们这里是在一个python交互she1l里面，最高主线程会- -直存在
print('child process exited' )

print('---------------------------------------------多线程多进程操作-----------------------------------------------------')