from functools import wraps
from collections import namedtuple


def simple_coroutine():
    '''
    最简单的协程例子
    '''
    print("-> 开始协程")
    x = yield
    print("收到了协程信号", x)


def simple_coro2(a):
    '''
    产生两个值的协程
    '''
    print("-> started: a = ", a)
    b = yield a
    print("-> received b = ", b)
    c = yield a + b
    print("-> received v =  ", c)


def coroutine(func):
    '''
    预激协程装饰器
    向前执行到第一个yield表达式 预激`func`
    '''
    @wraps(func)
    def primer(*args, **kwagrs):
        gen = func(*args, **kwagrs)
        next(gen)
        return gen
    return primer


@coroutine
def averager():
    '''
    计算移动平均值
    '''
    total = 0.0
    count = 0
    averager = None
    while True:
        term = yield averager
        total += term
        count += 1
        averager = total / count


Reuslt = namedtuple("Result", "count average")


@coroutine
def averager2():
    '''
    计算移动平均值
    '''
    total = 0.0
    count = 0
    averager = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        averager = total / count
    return Reuslt(count, averager)
