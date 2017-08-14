'''
欧几里得向量类

v1

'''

from array import array
import math


class Vector2d:
    typecode = 'd'  # 类属性，再实例和字节序列之间转换时会用到

    def __init__(self, x, y):  # 将坐标转换为浮点类型
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):  # 定义成可迭代类型，这样方便我们拆包 如 x,y = my_vector
        return (i for i in (self.x, self.y))

    def __repr__(self):  # {!r} 获取各个分量的表现形式，最后构造成一个字符串
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)

    def __str__(self):  # 从self的可迭代特性中，轻松可以得到一个元组，用于表示此类
        return str(tuple(self))

    def __bytes__(self):  # 先将typocode转换为字节序列，再迭代实例得到一个数组之后，再将该数组转换为字节序列
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):  # 简单的比较 有局限性 比如 Vector2d(3,4) == [3,4] 会返回True
        return tuple(self) == tuple(other)

    def __abs__(self):  # 取模
        return math.hypot(self.x, self.y)

    def __bool__(self):  # 0：false 1：True
        return bool(abs(self))

# test

# 实例的分类可以通过属性直接访问
v1 = Vector2d(3, 4)
print(v1.x, v1.y)

# 实例可以拆包成元组
x, y = v1
print(x, y)
print(v1)

# 通过eval函数，表明repr函数调用的实例得到的是对构造方法的准确表述
v1_clone = eval(repr(v1))
print(v1 == v1_clone)

# bytes函数会调用类的__bytes__方法来生成实例的二进制表现形式
octets = bytes(v1)
print(octets)
# 测试一下abs和bool方法
print(abs(v1))
print(bool(v1),bool(Vector2d(0,0)))


'''
OUT:
3.0 4.0
3.0 4.0
(3.0, 4.0)
True
b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
5.0
True False


'''