from bank import value

def test_value():
    assert value('HELLO') == 0
    assert value('HELLO, NEWMAN') == 0
def test_value2():
    assert value(' HELLO ') == 0
    assert value('HOW YOU DOING?') == 20
def test_value3():
    assert value("WHAT'S HAPPENING?") == 100
    assert value("WHAT'S UP") == 100







