#整数类型
a = 100
b = -100
c = 0xff00
print(a)
print(b)
print(c)

#浮点数
a = 1.23
b = -3.14
c = 0.000012
#等价于 c=1.2e-05
print(a)
print(b)
print(c)

#字符串(是否转义字符)
print('I\'m \"OK\"!')
print('I am learning \n Python now.')   #默认使用转义字符
print(r'I am learning \n Python now.')  #r''不使用转义字符
print('''line1
line2
line3''')   #输出多行字符串

#布尔值 True False
#布尔值运算符 and、or、not
boolean1 = 3>2
boolean2 = not 3
print(boolean1)
print(boolean2)

#空值
x = None
print(x)

#变量 -> 动态变量
a = 1
a = 'string'
print('python里的变量是动态变量，可以赋值不同类型的数据', 'a=', a)

#常量(命名常量用大写，但事实上仍然是一个变量)
PI = 1
PI = 3.1415926
print(PI)
print('地板除，结果取整（舍去小数）:', 10 // 3)  #地板除，结果取整（舍去小数）