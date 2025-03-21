from working import convert
import pytest
def main():
    test_Value_error1()
    test_Value_error2()
    test_Value_error3()
    test_Value_error4()
    test_Value_error5()
    test_Value_error6()
    test_Value_eroor7()

    test_convert()
def test_Value_error1():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
def test_Value_error2():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')
def test_Value_error3():
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')
def test_Value_error4():
    with pytest.raises(ValueError):
        convert('13 AM 17 PM')
def test_Value_error5():
    with pytest.raises(ValueError):
        convert('13 to 17')
def test_Value_error6():
    with pytest.raises(ValueError):
        convert('1317')
def test_Value_eroor7():
    with pytest.raises(ValueError):
        convert('22:00 AM - 24:00PM')



def test_convert():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10 AM to 8:50 PM') == '10:00 to 20:50'
    assert convert('10:30 PM to 8 AM') == '22:30 to 08:00'

if __name__ == "__main__":
        main()

