'''
变量的作用域
'''


def f1(a):
    print(a)
    print(b)


f1(3)


def f1(a):
    print(a)
    print(b)


b = 6
f1(3)

'''
OUT:
3
6
'''


def f1(a):
    print(a)
    print(b)
    b = 9


b = 6
f1(3)


def f1(a):
    global b
    print(a)
    print(b)
    b = 9


b = 6
f1(3)
print(b)
