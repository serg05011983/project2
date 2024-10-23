import pytest

# import random
from src.decorators import log

# if random.randint(0, 1) == 0:
filename = None
# else:
#    filename = "mylog.txt"


def test_log(capsys):
    """функция для тестирования работы декоратора логгирования"""

    @log(filename)
    def divider(x, y):
        print(f"\nfilename= {filename}\n")
        # some potentially failing operation
        return x / y

    assert divider(3, 1) == 3
    captured = capsys.readouterr()
    assert captured.out == "\nfilename= None\n\ntest_log.<locals>.divider OK\n\n"
    assert captured.err == ""
    assert divider(3, 0) == None
    captured = capsys.readouterr()
    assert (
        captured.out == "\nfilename= None\n\ntest_log.<locals>.divider error: division by zero Inputs: (3, 0)-{} \n\n"
    )
