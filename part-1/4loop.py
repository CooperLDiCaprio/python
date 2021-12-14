# TODO 循环
# TODO Python的循环有两种，一种是for...in循环 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
# TODO 在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
# TODO 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。

# TODO一
sums = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sums = sums + x
print(sums)

# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
print(list(range(5)))
# range(101)就可以生成0-100的整数序列，计算如下：
sums = 0
for x in range(101):
    sums = sums + x
print(sums)

# TODO 二
# 比如我们要计算100以内所有奇数之和，可以用while循环实现：
sums = 0
n = 99
while n > 0:
    sums = sums + n
    n = n - 2
print(sums)

# TODO 三
# 在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break   # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# TODO 四
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:   # 如果n是偶数，执行continue语句
        continue     # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)