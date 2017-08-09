'''
函数和参数
'''


def tag(name, *content, cls=None, **attrs):
    '''生成一个或者多个html标签'''

    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' {}="{}" '.format(attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<{}{}>{}</{}>'.format(name, attr_str, c, name) for c in content)
    else:
        return '<{}{} />'.format(name, attr_str)


# 传入单个定位参数，生成一个指定名称的空标签
print(tag('br'))
# 第一个参数后面的任意个参数会被*content捕获，存入一个元组
print(tag('p', 'hello,world'))
# 没有指定明确官架子的参数会给**attrs捕获，存入一个字典
print(tag('p', 'hello,world', id=333))
my_tag = {'name': 'img', 'little': 'sunset boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}
# 在my_tag前加入** 滋滋暗中的所有元素作为单个参数传入，同键名会绑定到对应的具名参数上，余下的会被**attrs捕获
print(tag(**my_tag))

'''
OUT：

<br />
<p>hello,world</p>
<p id="333" >hello,world</p>
<img class="framed"  little="sunset boulevard"  src="sunset.jpg"  />
'''
