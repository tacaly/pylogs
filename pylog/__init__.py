import sys


def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('[PYLog] Doing something.')


def windows_interaction():
    assert ('windows' in sys.platform), "Function can only run on Windows systems."
    print('[PYLog] Doing something on windows.')


def mac_interaction():
    assert ('mac' in sys.platform), "Function can only run on Mac systems."
    print('[PYLog] Doing something.')
