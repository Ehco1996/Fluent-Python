'''
with 语句的相关操作
'''


dirpath = '/Users/ehco/Documents/codestuff/Fluent-Python/第十五章上下文管理器和else块/'

with open(dirpath+'15-1.py', 'r') as f:
    src = f.read()

print(len(src))
print (f)
f.read()

'''
out:

394
<_io.TextIOWrapper name='/.../15-1.py' mode='r' encoding='UTF-8'>
ValueError: I/O operation on closed file.
'''