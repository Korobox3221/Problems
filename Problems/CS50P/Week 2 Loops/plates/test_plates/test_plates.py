from plates import is_valid
def main():
    test_valid()

def test_valid():
    assert is_valid('CS50') == True
    assert is_valid('ECTO88') == True
    assert is_valid('NRVOUS') == True

def test_invalid():
    assert is_valid('CS05') == False
    assert is_valid('50') == False

def test_invalid2():
    assert is_valid('CS50P2') == False
    assert is_valid('PI3.14') == False



def test_invalid3():
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False
if __name__ == "__main__":
        main()
