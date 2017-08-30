'''
多维向量类 v2

支持切片
'''

from array import array
import reprlib
import math
import numbers

class Vector:
    typecode = 'd'

    def __init__(self, components):
        # 用 _ 代表受保护的属性，把Vector的分量保存在一个数组之中
        self._components = array(self.typecode, components)

    def __iter__(self):
        # 通过_components 来构造一个迭代器
        return iter(self._components)

    def __repr__(self):
        # 使用reprlib.repr()函数来获取分量的有限长度的表现形式（防止出现1000维度的实例显示问题）
        components = reprlib.repr(self._components)
        # 通过字符串生成实例是 删掉【 之前和array（d）后面的
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        # 这里我们可以直接使用_components 来构建bytes对象
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        # 通过计算各个分量的平方和来算出绝对值（距离）
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)  # 获取实例的类型

        if isinstance(index, slice):  # 如果index参数值是切片的对象
            # 调用Vector的构造方法，建立一个新的切片后的Vector类
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):  # 如果参数是整数类型
            return self._components[index]  # 我们就对数组进行切片
        else:  # 否则我们就抛出异常
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # 直接将memview传给class即可，不用拆包
        return cls(memv)


# 现在我们的向量类就已经支持切片操作了
test = Vector([3, 4, 5])
print(test[-1])
print(test[:2])
print(test[1,2])


'''
OUT:
5.0
(3.0, 4.0)
Traceback (most recent call last):
TypeError: Vector indices must be integers
'''
