import sys


def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    logging.basicConfig(filename=loglinux,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    logging.info("[PYLog]Running log Planning linux")

    print('[PYLog]Doing something.')


def windows_interaction():
    assert ('windows' in sys.platform), "Function can only run on Windows systems."
    logging.basicConfig(filename=logwindows,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    logging.info("[PYLog]Running log Planning windows")
    print('[PYLog]Doing something on windows.')


def mac_interaction():
    assert ('mac' in sys.platform), "Function can only run on Mac systems."
    logging.basicConfig(filename=logmac,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    logging.info("[PYLog]Running log Planning mac")
    print('[PYLog]Doing something.')
