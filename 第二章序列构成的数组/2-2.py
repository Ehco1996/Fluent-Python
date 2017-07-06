'''
笛卡尔积

如果你需要一个列表，列表里是三种不同尺寸的衬衫，且每种衬衫都有两个颜色，
我们用下面的例子来生成一个笛卡尔积形式的列表
'''


# 用列表推导计算笛卡尔积：
colors = ['white', 'black']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)


# 如果你想依照尺寸为先进行列表的生成：
tshirts_size_first = [(color, size) for size in sizes for color in colors]
print(tshirts_size_first)


'''
列表推导的作用只有一个：生成列表！
如果想生成其他类型的序列，就需要用到「生成器」了

生成器表达式的语法和列表推导的方法相似，仅仅是把 [] 换成了（）
生成器表达式相对于列表推导来说，更加的「节省内存」
请下下面这个例子：
'''

# 用生成器表达式 计算笛卡尔积：

for tshirt in ('%s,%s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

'''
OUT:

white,S
white,M
white,L
black,S
black,M
black,L
'''