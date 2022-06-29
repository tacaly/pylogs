import logging
import sys


def error_logger():
    pylog = logging.getLogger()
    pylog.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('log.txt')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    pylog.addHandler(file_handler)
    pylog.addHandler(stdout_handler)

    # use pylog.info('This is a log message!')
    # use pylog.error('This is an error message.')


def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."

    print('[PYLog] Doing something. "Linux_28" ')


def windows_interaction():
    assert ('windows' in sys.platform), "Function can only run on Windows systems."

    print('[PYLog]Doing something on windows. "Windows_34" ')


def mac_interaction():
    assert ('mac' in sys.platform), "Function can only run on Mac systems."

    print('[PYLog] Doing something. "Mac_40" ')

def mac_interaction():
    assert ('pi' in sys.platform), "Function can only run on Pi systems."

    print('[PYLog] Doing something. "Pi_45" ')
