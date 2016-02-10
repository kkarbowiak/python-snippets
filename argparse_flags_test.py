import argparse

def main():
    parser = argparse.ArgumentParser(description='argparse script')

    parser.add_argument('-e', '--exe', action='store_true', help='copy executable')
    parser.add_argument('-l', '--lib', action='store_true', help='copy libraries')
    parser.add_argument('-x', '--xml', action='store_true', help='copy xml file')

    args = parser.parse_args()

    print 'e = ', args.exe
    print 'l = ', args.lib
    print 'x = ', args.xml


if __name__ == '__main__':
    main()
