# TODO 条件判断(Conditional  judgment)
# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。

# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

age = 10
if age >= 18:
    print('your age is', age)
    print('adult')

# TODO if判断条件还可以简写(只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False)比如写：
x = []
if x:
    print('True')
else:
    print('adult')

x = [123]
if x:
    print('True')
# adult
# True
