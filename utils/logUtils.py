import time
from maya import cmds


def _message(type_, msg, prefix=''):
    if prefix:
        s = '{0} : {1}'.format(prefix, msg)
    else:
        s = msg

    if type_ == 'warning':
        cmds.warning(s)
    elif type_ == 'error':
        cmds.error(s)
    elif type_ == 'info':
        print(s)


def warning(msg, prefix=''):
    _message('warning', msg, prefix)


def error(msg, prefix=''):
    _message('error', msg, prefix)


def info(msg, prefix=''):
    _message('info', msg, prefix)


def log(func):
    def wrapper(*args, **kwargs):
        print('')
        print('-' * 10)
        print('\'{0}\' starts.'.format(func.__name__))
        print('-' * 10)
        print('')
        start = time.time()
        result = func(*args, **kwargs)
        delta = time.time() - start
        print('')
        print('-' * 10)
        print('\'{0}\' ends. Took {1} sec'.format(func.__name__, delta))
        print('-' * 10)
        print('')
        return result
    return wrapper
