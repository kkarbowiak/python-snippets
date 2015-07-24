import functools


def main():
    vf0 = functools.partial(void_fun_0ary)
    vf1 = functools.partial(void_fun_1ary, 5)
    if0 = functools.partial(int_fun_0ary)
    if1 = functools.partial(int_fun_1ary, 7)
    lf0 = functools.partial(list_fun_0ary)
    lf1 = functools.partial(list_fun_1ary, 9)

    wrapper(vf0)
    wrapper(vf1)
    i0 = wrapper(if0)
    i1 = wrapper(if1)
    l0 = wrapper(lf0)
    l1 = wrapper(lf1)

    print 'i0', i0
    print 'i1', i1
    print 'l0', l0
    print 'l1', l1


def wrapper(function):
    return function()


def void_fun_0ary():
    print 'void_fun_0ary()'


def void_fun_1ary(arg1):
    print 'void_fun_1ary()', arg1


def int_fun_0ary():
    print 'int_fun_0ary()'
    return 3


def int_fun_1ary(arg1):
    print 'int_fun_1ary()', arg1
    return arg1


def list_fun_0ary():
    print 'list_fun_0ary()'
    return [1, 2, 3]


def list_fun_1ary(arg1):
    print 'list_fun_1ary()', arg1
    return [1, arg1, 2, 3]


if __name__ == '__main__':
    main()
