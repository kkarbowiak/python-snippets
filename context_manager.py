from __future__ import print_function, with_statement
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


def main():
    with context_mgr('c1') as c1:
        print('context c1 is named ' + c1.get_name())
        #raise RuntimeError('error')
        time.sleep(10)


if __name__ == '__main__':
    main()
