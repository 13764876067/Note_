#coding:utf-8

'''
1. python中的简单语句笔记
    赋值语句
    判断语句
    循环语句

'''

'''

1.赋值语句
    variable = object
    a = 1,2,3
    a,b,c = 1,2,3    
    a,_,c = 1,2,3
    a,*c = 4,5,6
    a = a + 1 => a += 1 :自增,自减,自乘,自除: += -= *= /=
    
    in ,is ,del
    
2.条件语句
    if...else...
    if...elif...elif...else...    
    a = 'python' if 4 > 3 else 'physics!'

3.循环语句
    for循环语句
    for i in 'abcdefg' : (必须为可迭代对象即包含_iter迭代器) 
        print(i)
        
    for i in range(100) : #range():创建一个值区间
        print(i)
        
    常用的几个函数
    range(4)=>0,1,2,3   使用时才会被读到内存
    range(start,stop,step) => range.object   
    list(range(100))
    
    zip(a,b):拉链操作 序列拉链, 左基准
    
    enumerate():枚举操作:返回所有元素及其下标
    
    列表解析*
    [i**2 for i in range(10)] :10以内数的平方
    [i for i in range(100) if i%3==0] :100以内3的倍数
    
    while循环语句:
    a = 0
    while a < 3:
        a += 1

    break,continue关键字
    跳出整个循环:break
    跳出本次循环:continue
        
4.其他模块引入
    import random
    import math
    random.randint(1,10):随机生成1-10的整数
    math.pi:π
    round():四舍五入
    abs():绝对值
    
'''

print('---------------------------------------------赋值语句  部分-----------------------------------------------------')

a,b,c = 1,2,3
print(a,b,c)

d = 1,2
print(d)

e,f = 4,5
print(e,f)

a,_,c = 1,2,3
print(a,c)

a,*c = 4,5,6
print(a,c)

a += 1
print(a)

print('---------------------------------------------赋值语句  部分-----------------------------------------------------')

print('---------------------------------------------判断语句  部分-----------------------------------------------------')

a = 5
if a > 3 :
    print('>')
else :
    print('<')
print('ok!')

s0 = 'abcdef'
if 'a' in s0 :
    print('a')
elif 'b' in s0 :
    print('b')
elif 'g' in s0 :
    print('g')
else :
    print('other')
print('finish!')

a = 'python!' if 4 > 3 else 'physics!'
print(a)

print('---------------------------------------------判断语句  部分-----------------------------------------------------')

print('---------------------------------------------循环语句  部分-----------------------------------------------------')

for i in 'abcdefg' :
    print(i)

dic = dict([('a',1),('b',2),('c',3)])
#for k in dic :
#    print(k,dic[k])

for k in dic :
    #k = dic[k]  dt[dic[k]] = k
    print(k,dic[k])
print(dic)

for k,v in dic.items():
    print(k,v)

import random as rd
ls = []
dic = {}

for i in range(100) :
    ls.append(rd.randint(1,100))
print(ls)

for v in ls :
    if v in dic :
        dic[v] += 1
    else :
        dic[v] = 1
print(dic)

a = [1,2,3]
b = [3,4,5]
c = []
for x,y in zip(a,b) :
    c.append(x+y)
print(c,type(c))

m = {1,2,3}
n = {1,2,3}
f = set()
#print(zip(m,n),set(zip(m,n)))
for x,y in zip(m,n) :
    f.add(x+y)
print(f,type(f))

print(enumerate(a),list(enumerate(a)))

number = rd.randint(1,100)
while True :
    num_input = input('input a number:')
    if not num_input.isdigit():
        print('please input Interger.')
    elif int(num_input) < 0 or int(num_input) >= 100:
        print('The number should be in 1 to 100.')
    else:
        if number == int(num_input):
            print('OK')
        elif number > int(num_input):
            print('your number is smaller')
        else:
            print('your number is bigger')


print('---------------------------------------------循环语句  部分-----------------------------------------------------')