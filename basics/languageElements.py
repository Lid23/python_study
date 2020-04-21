"""
# 变量
- 整形：int
- 浮点型：float
- 字符串型：'hello', "hello", 支持三个单引号和三个双引号
- 布尔型； True, False
- 复数型： 3+5j
# 类型
-
"""

a = 321
b = 12
print(a + b)
print(a - b)
print(a * b)
print(a / b)


# type函数对变量的类型进行检查
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, python'
e = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 使用Python内置的函数对变量类型进行转换
# a = int(input('a = '))
# b = int(input('b = '))

print('%d + %d = %d' % (a, b, a+b))
print('%d - %d = %d' % (a, b, a-b))
print('%d * %d = %d' % (a, b, a*b))
print('%d / %d = %d' % (a, b, a/b))
print('%d // %d = %d' % (a, b, a//b))
print('%d %% %d = %d' % (a, b, a%b))
print('%d ** %d = %d' % (a, b, a**b))

"""
赋值运算符和复合赋值运算符
Version: 0.1
Author: Noodles
"""
a += b
a *= a + 2
print(a)

"""
比较运算符
Version: 0.1
Author: Noodles
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 = ', flag0)
print('flag1 = ', flag1)
print('flag2 = ', flag2)
print('flag3 = ', flag3)
print('flag4 = ', flag4)
print('flag5 = ', flag5)


"""
将华氏温度转为摄氏温度
Version: 0.1
Author: Noodles
"""
f = float(input("请输入华氏温度:"))
c = (f - 32) / 1.8
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

"""
输入圆的半径计算周长和面积
Version: 0.1
Author: Noodles
"""
import math
r = float(input("输入半径："))
s = math.pi * r * 2
area = math.pi * r * r
print(f'周长：{s:.2f}， 面积：{area:.2f}')

"""
输入年份，判断是否闰年
Version: 0.1
Author: Noodles
"""
year = int(input("输入年份："))
id_leap = year % 4 == 0 and year % 100 != 0 or \
    year % 400 == 0
print(id_leap)



