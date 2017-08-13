'''
变量不是盒子
'''

a = [1,2,3]
b = a 
b.append(4)
print(a)

'''
OUT:
[1, 2, 3, 4]
'''