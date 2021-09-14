import pylog
import pytest


def test_func_fast():
    pylog.info('test module log message!')
    pass


@pytest.mark.slow
def test_func_slow():
    pass