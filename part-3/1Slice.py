# TODO 切片(Slice)
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前3个元素，应该怎么做？
r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)

# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
print(L[0:3])
# 如果第一个索引是0，还可以省略：
print(L[:3])

# 既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片(记住倒数第一个元素的索引是-1。)
print(L[-1:])

L = list(range(100))
# 可以通过切片轻松取出某一段数列。比如前10个数：
print(L[0:10])
# 后10个数：
print(L[-10:])
# 前10个数，每两个取一个：
print(L[0:10:2])
# 前10个数，再从里去前五个
print(L[11:20][0:5])
# 所有数，每5个取一个：
print(L[::5])
# 甚至什么都不写，只写[:]就可以原样复制一个list：
print(L[:])
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])
