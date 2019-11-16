# ASCII、Unicode和UTF-8的关系
# ASCII编码是1个字节，而Unicode编码通常是2个字节。
# 出现了把Unicode编码转化为“可变长编码”的UTF-8编码。
# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

# Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))


# bytes类型的数据用带b前缀
print('ABC')
print(b'ABC')
# print(b'中文')  报错，原因是bytes转1个字节，一个中文两个字节

# 切换编码
code1 = '中文'  
# code1 = '\u4e2d\u6587'  # 等价
code2 = '中文'.encode('utf-8')
code3 = '中文'.encode('gb2312')
print('Unicode编码：', code1)
print('utf8编码：', code2)
print('gb2312编码：', code3)


# len()函数计算的是str的字符数，
# 如果换成bytes，len()函数就计算字节数：
num1 = len('ABC')
num2 = len('中文')
print(num1)
print(num2)

# 格式化
# 在字符串内部
# %s表示用字符串替换，%d表示用整数替换
# %f表示用浮点数替换, %x表示用十六进制整数替换
# 有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
# 如果只有一个%?，括号可以省略。
print('Hello, %s' % 'Lmy')
print('Hi, %s, you have ¥%d+ .' % ('Lmy', 10000))










