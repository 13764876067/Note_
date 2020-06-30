#coding:utf-8

'''

1.python 中的综合示例部分

遍历文件目录操作统计所有目录包括子目录大小尺寸
    基础版本
    comprehension[列表解析]递归版本
    map,filter特殊函数递归版本
    多线程版本
    os.walk

'''


'''

1.有一个目录,这里面的目录有多层子目录,每一层子目录里包含若干文件,
要求统计这个目录下所有文件的尺寸?

    基础递归版本[没有使用列表解析]
        先列出文件目录遍历判断如果是目录就递归否则sum(求和size)

    comprehension[列表解析]递归版本
        先列出文件目录遍历判断如果是目录就递归否则sum(求和size)

    map,filter特殊函数递归版本
        1.利用filter过滤本层目录出文件,map求和size
        2.filter过滤出本层目录的目录,map映射递归

    多线程递归版本multiprocessing,ThreadPool利用线程池加快
    递归的效率

    使用os.walk的方法遍历返回目录中所有内容(路径,目录名,文件名)
    os.walk()方法使用
    
'''

print('---------------------------------------------遍历文件目录操作-----------------------------------------------------')

import os

#基础递归版本
def dir_size4(d):
    '''
    递归版本.
    这是最基础的版本，没啥好说的，需要注意的是，既然用递归，
    就不要考虑全局变量啥的了，累计的size, 直接作为返回值就好了。
    :param d:
    :return:
    '''
    #读取文件信息
    dlist = os.listdir(d)
    #遍历所有内容
    allsize = 0
    for i in dlist:
    #为遍历的文件添加目录
        file = os.path.join(d, i)
        #判断是否是文件 求size
        if os.path.isfile(file):
            m = os.path.getsize(file)
            allsize = m
        #判断是否是目录 调用自己
        if os.path.isdir(file):
            allsize += dir_size4(file)
    return allsize
#print('dir size:\t{}'.format(dir_size4("E:\\APP")))

#递归comprehension[列表解析]版本
def dir_size3(d):
    '''
    递归comprehension版本.
    这个是逼格稍微高点的版本，这里的重点就是comprehension了 。
    :param d:
    :return:
    '''
    dlist = [os.path.join(d, i) for i in os.listdir(d)]#先列出文件目录
    allsize = sum([os.path.getsize(file)
        for file in dlist if os.path.isfile(file)])#遍历判断如果是文件就sum(求和size)
    allsize += sum([dir_size3(file)
        for file in dlist if os.path.isdir(file)])#遍历判断如果是目录就递归
    return allsize
#print('dir size:\t{}'.format(dir_size3("E:\\APP")))

def dir_size2(d):
    '''
    递归comprehension版本.
    另-种蛋疼的写法，吓唬人玩行， 般别吃饱 了撑的用这种写 法.
    :param d:
    :return:
    '''
    return sum([dir_size2(f) if os.path.isdir(f) else os.path.getsize(f)
    for f in [os.path.join(d, i) for i in os. listdir(d)]])
    #从右向左解析看 先列出文件目录遍历判断如果是目录就递归否则sum(求和size)
#print( 'dir size:\t{}'. format(dir_size2("E:\\APP")))

#利用map和filter特殊函数进行选择操作
def dir_size1(d):
    '''
    递归map
    filter版本.
    简洁的一逼，刚开始没想起来。
    :param d:
    :return:
    '''
    dlist = [os.path.join(d, i) for i in os.listdir(d)]#列出目录+文件
    allsize = sum(map(os.path.getsize, filter(os.path.isfile, dlist)))#filter过滤出文件,map求和
    allsize += sum(map(dir_size1, filter(os.path.isdir, dlist)))#filter过滤出目录,map映射递归
    return allsize
#print('dir size:\t{}'.format(dir_size1("E:\\APP")))

#多线程递归版本
from multiprocessing.pool import ThreadPool
def dir_size0(d):
    '''
    多线程递归版本.
    1,在这里，这个版本反而比单线程的慢，因为我本地是SSD，而且目录也没有大到离谱，线程切
    开销已经完全抵消了多线程的I0效率优势。如果是统计NFS,大规模的磁盘阵列啥的，可能
    会有些微薄的优势。
    2,因为有递归，所以不能用多进程。python里面的子 进程不能再有子进程，会报错的。不要在
    的场合使用多进程，除非小心的设计一下。
    这里其实还有-种思路是先用walk列出所有的文件目录，再用多线程或者多进程统计文件
    是列出所有目录这个动作本身就要遍历所有文件了，所以这种做法在这个场景下其实效率7
    :param d:
    :return:
    '''
    dlist = [os.path.join(d, i) for i in os.listdir(d)]#列出该路径下文件和目录
    allsize = sum([os.path.getsize(file)
                   for file in dlist if os.path.isfile(file)])#将文件相加
    p = ThreadPool()#开启线程池
    ret = p.map(dir_size0,[file
                          for file in dlist if os.path.isdir(file)])#递归判断是否为目录,为目录就递归再算, map映射 每个元素到函数
    p.close()#关闭线程池
    p.join()#等待
    allsize += sum(ret)#相加所有结果
    return allsize
#print('dir size:\t{}'.format(dir_size0("E:\\")))

#使用os.walk的方法遍历返回目录中所有内容(路径,目录名,文件名)
def dir_size(d):
    '''
    walk版本
       For each directory in the directory tree rooted at top (including top
    itself, but excluding '.' and '..'), yields a 3-tuple
        dirpath, dirnames, filenames

    这个版本没有递归,
    :return:
    '''
    allsize = 0
    for r,ds,fs in os.walk(d):
        allsize += sum(os.path.getsize(file) for
        file in [os.path.join(r,f) for f in fs]) # join=>将文件目录和文件连接起来
    return allsize
#print(help(os.path.join))
#print([os.path.join("e:", "abc")]) => ['e:abc']
#print('dir size:\t{}'.format(dir_size('E:\\')))

print('---------------------------------------------遍历文件目录操作-----------------------------------------------------')