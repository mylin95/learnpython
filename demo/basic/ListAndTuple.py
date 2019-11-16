
# Python内置的一种数据类型是列表：list。
# list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))

# list越界会报IndexError错误
# 倒序取数：获取倒数第i个元素：classmates[-i]
# print(classmates[3]) # 越界报错
print(classmates[-1])
print(classmates[-2])

# list是一个可变的有序表
# 1.1 尾加 可以往list中追加元素到末尾：
classmates.append('Adam')
print(classmates)
# 1.2 加
classmates.insert(1, 'Jack')
print(classmates)
# 2.1 尾删 要删除list末尾的元素，用pop()方法：
lastEle = classmates.pop()
print(lastEle)
print(classmates)
# 2.2 删 
delEle = classmates.pop(1)
print(delEle)
print(classmates)
# 3.1替换
classmates[1] = 'Amy'
print(classmates)

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print(L)
# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
# list的元素包含list，拆开写更优雅
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s)

# list的长度
print(len(s))

# 另一种有序列表叫元组：tuple
# tuple类似list，不过它是只读的，一旦初始化不可更改
classmates = ('Michael', 'Bob', "Tracy")
# classmates[1] = 'Amy' # 不可赋值，报错
print(classmates)
t = ()      # 定义空的tuple
t = (1)     # 定义只有一个元素1的元组(tuple)   ——有歧义
t = (1, )   # 定义只有一个元素的元组(tuple)
t = ('a', 'b', ['A', 'B'])  # 定义只读的二维数组
t[2][0] = 'X'               # 内嵌一个list，它的值可以更改
t[2][1] = 'Y'
print(t)






