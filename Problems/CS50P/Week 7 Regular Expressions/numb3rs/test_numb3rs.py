from numb3rs import validate
def main():
    test_ip()


def test_ip():
    assert validate('127.0.0.1')== True
    assert validate('255.255.255.255') == True
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False
    assert validate('256.255.255.255') == False
    assert validate('255.300.261.275') == False










if __name__ == "__main__":
    main()
