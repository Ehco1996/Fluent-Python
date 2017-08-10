'''
装饰器基础
'''

def decorate(func):
    def inner():
        print('running inner')
    return inner

@decorate
def target():
    print('running target')



target()

'''
OUT:
running inner
'''

decorate(target())