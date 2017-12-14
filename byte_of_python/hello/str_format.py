#coding: utf-8
age = 20
name = 'Swaroop'

#format格式化参数，变量的设置
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('why is {0} playing with that python?'.format(name))

#对于浮点数，保留小数点后三位
print('{0:.3f}'.format(1.0/3))

#下划线填充文本，使字符串位于中间
#使用(^)定义字符串长度
print('{0:_^7}'.format('hello'))

#print会自带一个'\n'换行,如果不想换行可以通过end指定以空白结尾
print('a', end=' ')
print('b')

