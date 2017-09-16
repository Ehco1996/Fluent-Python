def gen_AB():
    print ('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


for c in gen_AB():
    print(c)

'''
Out:

start
A
continue
B
end
'''