'''
单词序列v4
'''

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        # 返回一个字符串列表、元素为正则所匹配到的非重叠匹配】
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        # 该函数用于生成大型数据结构的简略字符串的表现形式
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        '''惰性生成器版本'''
        for match in RE_WORD.finditer(self.text):
            yield match.group()

# TEST 该类是否能够完成迭代


s = Sentence('Ehco is a good Python coder')
print(s)
for word in s:
    print(word)

'''
OUT:

Sentence('Ehco is a good Python coder') # 该字符串是有repr方法生成的
Ehco    # 可以看到，我们的Sentence类已经支持迭代输出了
is
a
good
Python
coder
'''
