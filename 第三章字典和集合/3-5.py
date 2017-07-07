import collections

ct = collections.Counter('asdfghjk')
print(ct)
ct.update('qweqweqweqwe')
print(ct)
print(ct.most_common(2))

'''
Counter({'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1})
Counter({'q': 4, 'w': 4, 'e': 4, 'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1})
[('q', 4), ('w', 4)]
'''