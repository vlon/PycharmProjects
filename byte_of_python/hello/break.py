# coding: utf-8

#如果中断了for或者while循环,则else模块将不被执行

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')