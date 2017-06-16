'''
通过Python内置的魔法方法（magic/dunder method）
创建一个 Python风格的纸牌


TEST DOC：

# 生成一张黑桃2
Card('2','spade')

# 生成一组法式纸牌
deck = FrenchDeck()

# 打印出所有的纸牌
print(deck._cards)

# 打印出纸牌的个数
print(len(deck))

# 迭代输出纸牌
for card in deck:
    print(card)

# 按照花色排序输出纸牌
for card in sorted(deck,key=sort):
    print(card)

'''

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck():
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 生成纸牌的序号
    suits = 'spades diamons clubs hearts'.split()

    def __init__(self,):
        '''
        初始化一整套法式纸牌
        '''
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        '''
        返回这一套卡组的长度
        '''
        return len(self._cards)

    def __getitem__(self, position):
        '''
        返回卡组的位置
        方便Python对其进行切片的操作
        并且使得这个Card对象时一个可迭代的对象
        '''
        return self._cards[position]


# 表明不同花色的值
suit_values = dict(spades=3, hearts=2, diamons=1, clubs=0)


def sort(card):
    '''
    对card的顺序，按照花色进行排序
    '''
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
