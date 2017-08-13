'''
标识、相等性、别名
'''

ehco = {'name':'ehco','age':'21'}
xiaozhou = ehco

print(xiaozhou == ehco )
print(xiaozhou is ehco)
print(id(xiaozhou),id(ehco))

fake_ehco = {'name':'ehco','age':'21'}
print(fake_ehco==ehco)
print(fake_ehco is ehco)
print(id(fake_ehco),id(ehco))


'''
OUT：
True
True
4477069280 4477069280

True
False
4561643560 4561643488
'''