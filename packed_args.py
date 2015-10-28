def func(pos1, pos2, *args):
    print 'func(', pos1, pos2
    for a in args:
        print ',', a
    print ')'


def main():
    args = ['uno', 'duo', 'tres']
    func('pos1', 'pos2', *args)


if __name__ == '__main__':
    main()
