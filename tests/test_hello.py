import hello


def test_says_world():
    assert hello.say_what() == 'world'


def test_fail():
    assert hello.say_what == 'hey'