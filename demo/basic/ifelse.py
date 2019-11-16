
# if语句
# python对缩进要求严格，if语句里必须缩进
age = 5
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('kid')

# if语句简写
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = input('请输入数字：')
if x:
    print('True')

# 再议input
# input()：用户输入的值是str数据类型
s = input('birth year: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

#int(s)强转成int类型，如果强转失败需要捕获异常，容后再议







