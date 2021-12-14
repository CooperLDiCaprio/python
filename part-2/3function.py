# TODO 函数的参数 Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，
#  还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# TODO 一、默认参数
def power(x):
    return x * x

print(power(5))

# 默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5,3))

# TODO 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))

print(add_end())
# 但是，再次调用add_end()时，结果就不对了：
print(add_end())
print(add_end())

# 很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())

# TODO 二、可变参数


# TODO 三、关键字参数

# TODO 四、命名关键字参数

# TODO 五、参数组合
