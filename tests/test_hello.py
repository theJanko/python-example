import hello


def test_anything():
    print("zad 5")
    assert hello.anything() == 'print'

def test_says_world():
    assert hello.say_what() == 'world'

"""
def test_fail():
    assert hello.say_what == 'hey'
"""

def test_check_one():
    assert hello.one() == 3

def test_check_two():
    assert hello.two() == "code"

def test_check_three():
    assert hello.three() == 8

def test_check_four():
    assert hello.four() == "zadanie 5."