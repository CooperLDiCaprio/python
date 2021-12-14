# TODO dictionary（词典）
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，
# 所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

# TODO 关于字符串类型数据不可变对象
# str是不变对象，而list是可变对象。
# 对于不可变对象，比如str，对str进行操作呢：
a = 'abc'
print(a.replace('a', 'A'))
# 'Abc'
print(a)
# 'abc'
# 要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：
# 当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
# 相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：
# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# TODO 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['Adam'] = 67
print(d)

for i in d:
    print(i)
# Michael
# Bob
# Tracy
# Adam

for i in d:
    print(d[i])
# 95
# 75
# 85
# 67

# TODO 要避免key不存在的错误，有两种办法:
#  一是通过in判断key是否存在
#  二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
if 'Tracy' in d:
    print("Tracy is score:%d" % d['Tracy'])
# Tracy is score:85

print(d.get('JIm'))
# None

# TODO 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Tracy')
print(d)

s = set([1, 2, 3])
print(s)
# {1, 2, 3}
# 传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的

# TODO 没有重复的key
s = set([1, 1, 2, 2, 3, 3])
print(s)
# {1, 2, 3}

# TODO 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
# TODO 通过remove(key)方法可以删除元素：
s.remove(3)
print(s)

# TODO set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)