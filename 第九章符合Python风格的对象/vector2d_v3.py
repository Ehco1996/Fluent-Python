'''
欧几里得向量类

v3

'''

from array import array
import math


class Vector2d:
    typecode = 'd'  # 类属性，再实例和字节序列之间转换时会用到

    @classmethod  # 类方法的装饰器
    def frombytes(cls, octets):
        typecode = chr(octets[0])  # 从二进制码里的第一位转换为tyoecode
        # 使用传入的字节序列构造一个memoryview，并使用typecode转换
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)  # 拆包转换后的参数，并返回构造后的实例

    def __init__(self, x, y):  # 将坐标转换为浮点类型
        # 使用两个先导下划线将变量标记为私有 【记住！只是标记，主要是同志开发人员，类似于常量使用大写字母标注】
        self.__x = float(x)
        self.__y = float(y)

    @property  # 用该装饰器将读值方法标记为特性
    def x(self):  # 读值方法和公开属性同名，都是x
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        # 读取x、y的分量的时候，只读取公开属性，这样来保持私有属性的不变
        return (i for i in (self.x, self.y))

    def __hash__(self):
        # 为了保证散列值是固定不变的，我们首先得抱着所有属性的变。 
        # 根据__has__文档的要求，我们通常使用异或运算符 ^ 来混合分量的散列值
        return hash(self.x) ^ hash(self.y)

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
v1 = Vector2d(3, 4)
set([v1])
v1.x = 1

'''
OUT:
v1.x = 1
AttributeError: can't set attribute
'''
