import logging


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.NOTSET, datefmt='%Y-%m-%d %H:%M:%S')
    logging.debug('this is a debug message')
    logging.info('this is an info message')
    logging.warning('this is a warning message')
    logging.error('this is an error message')
    logging.critical('this is a critical message')
    try:
        raise RuntimeError('error')
    except:
        logging.exception('this is an exception message')

if __name__ == '__main__':
    main()
