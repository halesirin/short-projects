
#unit tests to check the program "ipvalidate"
from ipvalidate import validate

def test_dot():
    assert validate("222222") == False
def test_correct():
    assert validate("222.222.222.222") == True
def test_slot():
    assert validate("222.222.222") == False
def test_range():
    assert validate("222.222.222.265") == False
def test_letter():
    assert validate("kkk.222.222.265") == False