'''
简单装饰器的实现
'''

import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)  # 装饰被装饰的函数

        timepassed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)

        print('[{:.8f}s]   {}({})  -> {}'.format(timepassed, name, arg_str, result))
    return clocked


@clock
def sleep(sec):
    time.sleep(sec)


sleep(0.123)


@clock
def Double(n):
    return n + n


Double(6)

'''
OUT：

[0.12343142s]   sleep(0.123)  -> None
[0.00000404s]   Double(6)  -> 12

'''
