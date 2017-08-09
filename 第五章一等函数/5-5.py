'''
自定义可调用类型
'''

import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick form empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))

print(bingo.pick())
print(bingo())

'''
OUT：
1
2
'''

