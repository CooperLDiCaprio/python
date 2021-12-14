# TODO Python内置了很多有用的函数，我们可以直接调用(http://docs.python.org/3/library/functions.html#abs)
# 可以在交互式命令行通过help(abs)查看abs函数的帮助信息。

help(abs)
# Help on built-in function abs in module builtins:
#
# abs(x, /)
#     Return the absolute value of the argument.

print(abs(-20))
# 20

# abs(1, 2)
# Traceback (most recent call last):
#   File "E:/Python/workspaces/python/part-2/function.py", line 13, in <module>
#     abs(1, 2)
# TypeError: abs() takes exactly one argument (2 given)


print(max(2, 3, 1, -5))

# TODO 数据类型转换
#  Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

# TODO 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs  # 变量a指向abs函数
a(-1)    # 所以也可以通过a调用abs函数
print(a(-1))


# 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
