
# 循环 for ... in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 计算1+2+...+10
# 缩进不同，代码意义不同
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum += x
    # print(sum) 此处语句在循环体内
print(sum)  # 此处语句在循环体外

# 计算1+2+...+100
# range(): 自动生成整数序列
# range(5) <=> [0, 1 , 2, 3, 4]
sum = 0
for x in range(101):
    sum += x
print(sum)

#while语句
# 计算100以内的奇数和
sum = 0
n = 99
while n > 0:
    sum += n
    n = n - 2
print(sum)

# break语句
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1   #n++ python不存++语句
print('END break')

# continue语句
# 打印1-10内的奇数
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
print('END continue')

# 死循环
# while 1:
#     print(1)






