import random
import sys


def main():
    input, output = _get_inout(sys.argv)
    lines = open(input).readlines()
    random.shuffle(lines)
    open(output, 'w').writelines(lines)


def _get_inout(argv):
    if len(argv) == 3:
        return argv[1], argv[2]
    else:
        raise RuntimeError('You need to pass input and output file names')


if __name__ == '__main__':
    main()
