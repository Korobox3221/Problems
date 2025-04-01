from fuel import gauge, convert
import pytest
def main():
    test_convert()
    test_zero_division()
    test_value_error()

def test_zero_division():
   with pytest.raises(ZeroDivisionError):
       convert('1/0')
a
    with pytest.raises(ValueError):
        convert('cat/dog')

def test_convert():
    assert convert('3/4') == 75 and gauge(75) =='75%'
    assert convert('1/3') == 33 and gauge(33) == '33%'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'


if __name__ == "__main__":
        main()
