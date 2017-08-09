'''
函数也是对象
'''


def factorial(n):
    '''
    return n
    '''
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial.__doc__)

print(type(factorial))

print(factorial(3))

'''
OUT

    return n

<class 'function'>
6
'''

# 列表推导式的使用
fact = factorial

print(list(map(fact, range(6))))

print([fact(n) for n in range(6)])

'''
OUT:
[1, 1, 2, 6, 24, 120]
[1, 1, 2, 6, 24, 120]
'''
