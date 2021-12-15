import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 6)
print(r)


# TODO 一：默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(6, 3))


# TODO 二、可变参数(允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple(初始化后，不可更改的List))
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


num = [1, 2, 4, 5]
print(calc(num[0], num[1], num[2]))
print(calc(*num))


# TODO 三、关键字参数(关键字参数允许你传入0个或任意个含参数名的参数,这些关键字参数在函数内部自动组装为一个dict(Map))
def person(name, age, **kwargs):
    print('name:', name, 'age:', age, 'other:', kwargs)


print(person("Jack", 23, address="Beijing", cellphone='1865598019'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=extra['city'], job=extra['job']))

print(person('MaYun', 24, **extra))


# TODO 四、命名关键字参数(限制关键字参数名)
def person(name, age, *, city, job):
    print(name, age, city, job)


print(person("Cooper", 32, city='HeFei', job='Engineer', cellphone='1865598019'))
# Traceback (most recent call last):
#   File "E:/Python/workspaces/python/part-2/3demo.py", line 58, in <module>
#     print(person("Cooper", 32, city='HeFei', job='Engineer', cellphone='1865598019'))
# TypeError: person() got an unexpected keyword argument 'cellphone'


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


print(person('Jack', 24, city='Beijing', job='Engineer'))


# TODO 五、参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
def f1(a, b, c=0, *args, **kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kwargs =', kwargs)


def f2(a, b, c=0, *, d, **kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kwargs =', kwargs)


print(f1(1, 2))
num = [1, 2, 4, 5]
print(f1(1, 3, 4, *num))
print(f1(1, 3, 4, 1, 2, 4, 5))
print(f1(1, 3, 4, *num, age=23))

print(f2(1, 2, 4, d=23, age=23))

# args = [1, 2, 3]
args = (1, 2, 3, 4)
kwargs = {'age': 23}
print(f1(*args, **kwargs))

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))

