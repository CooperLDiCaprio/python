# TODO 使用list和tuple
# ist是一种有序的集合，可以随时添加和删除其中的元素。
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改。

classmates = ['Michael', 'Bob', 'Tracy']

# TODO 数组下标第一个值
print(classmates[0])
# Michael

# TODO 数组下标最后一个值
print(classmates[-1])
# Tracy
# TODO 以此类推，可以获取倒数第2个、倒数第3个：
print(classmates[-2])
# Bob
print(classmates[-3])
# Michael

# TODO 数组下标越界
print(classmates[3])
# Traceback (most recent call last):
#   File "E:/Python/workspaces/hello/collection.py", line 6, in <module>
#     print(classmates[3])
# IndexError: list index out of range

# TODO 数组追加数据
classmates.append('Adam')
print(classmates)

# TODO 可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'Jack')
print(classmates)

# TODO 要删除list末尾的元素，用pop()方法：
classmates.pop()
print(classmates)

# TODO 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
print(classmates)

# TODO 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
print(classmates)

# TODO list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print(L)

# TODO list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)

# TODO 要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s)


# TODO 元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
#  classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# TODO 当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print(t)

# TODO 如果要定义一个空的tuple，可以写成()：
t = ()
print(t)

# TODO 要定义一个只有1个元素的tuple，如果你这么定义：
t = (1)
print(t)
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)

# TODO 最后来看一个“可变的”tuple：
t = ('a', 'b', ['A', 'B'])
t[1] = 'c'
# Traceback (most recent call last):
#   File "E:/Python/workspaces/hello/collection.py", line 83, in <module>
#     t[1] = 'c'
# TypeError: 'tuple' object does not support item assignment
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
