from __future__ import print_function, with_statement
from contextlib import contextmanager
import time


class context_mgr:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('context_mgr.enter: ' + self.name)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('context_mgr.exit:  ' + self.name)

    def get_name(self):
        return self.name


@contextmanager
def mgr(name):
    try:
        print('decorated_mgr.enter: ' + name)
        yield
    finally:
        print('decorated_mgr.exit:  ' + name)


def ctx_mgr_test():
    with context_mgr('c1') as c1:
        print('context c1 is named ' + c1.get_name())
        #raise RuntimeError('error')
        time.sleep(10)


def dec_mgr_test():
    with mgr('c2') as c2:
        print('context c2')
        #raise RuntimeError('error')
        time.sleep(10)


def main():
    ctx_mgr_test()
    dec_mgr_test()


if __name__ == '__main__':
    main()
