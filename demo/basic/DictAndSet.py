
# dict
# dict全称dictionary，在其他语言中也称为map.
# 使用键-值（key-value）存储，具有极快的查找速度。
# dict的键值对存放是 无序的

# dict初始化，取值
dict1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dict1['Michael'])
print(dict1)
# 增、替换
dict1['Amy'] = 100
print(dict1['Amy'])
# 删
delEle = dict1.pop('Amy')
print(delEle)
print(dict1)
# 取值1：不存在key，报错
# print(dict1['Jack'])
# 可判断是否存在key
print('Amy' in dict1)
# 取值2：get()方法
print(dict1.get('Amy'))
print(dict1.get('Jack'))        #dict取值，为空则返回None
print(dict1.get('Jack', -1))    #dict取值，为空则返回默认值


# set
# set和dict类似，也是一组key的 集合
# 但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3])
print(s)
s = set([1, 1, 2, 2, 3, 3])
print(s)
# 增，重复加没有意义
s.add(4)
s.add(4)
print(s)
# 删，如果不存在key，删除报错
s.remove(4)     # 不能获取删除的值
# s.remove(4)   # 重复删，报错
print(s)
# set可以添加list类型吗？
# 不可以，set和dict一样，不可放入可变对象
# list1 = ['a', 'b', 'c']
# s.add(list1) # 报错
# print(s)

# 再议不可变对象
# list：可变对象
a = ['c', 'b', 'a']
a.sort()    # 对list a排序
print(a)
# str：不可变对象
a = 'abc'
# a = 'aaa'   # 变量明明是可变的啊
# print(a)
aChanges = a.replace('a', 'A')
print(a)
print(aChanges)





