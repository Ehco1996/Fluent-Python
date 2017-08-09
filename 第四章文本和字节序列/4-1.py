'''
编码和解码
'''

s = 'hello the world'
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

cn = "中国"
# gbk 和 gb2312 都是在win系统下使用较多的中文编码
d = cn.encode('gbk')
print (d)
print(d.decode('gb2312'))

'''
OUT :

b'hello the world'
hello the world
b'\xd6\xd0\xb9\xfa'
中国
'''