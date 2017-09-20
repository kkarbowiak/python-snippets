import functools


def foo():
    print('foo()')

def bar(arg):
    print('bar(' + arg + ')')

def executor(fun=lambda: None):
    fun()

executor()
executor(foo)
executor(functools.partial(bar, 'arg'))
