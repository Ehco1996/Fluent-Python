'''
else语句的应用
'''

# 在循环中使用else模块
# 当遍历整个列表都没有找到我们想要的元素时，抛出异常
my_list = ['banana', 'orange']
for item in my_list:
    if item == 'apple':
        break
else:
    raise ValueError('can not find apple')


# 在try except模块中使用else块
try:
    dangerous_call()
    after_call()
except OSError:
    log('OSerror')

try:
    dangerous_call()
except OSError:
    log('OSerror')
else:
    after_call()
    