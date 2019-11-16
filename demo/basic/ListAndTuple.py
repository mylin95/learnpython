
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










