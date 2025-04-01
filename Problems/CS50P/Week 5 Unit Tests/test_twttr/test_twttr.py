from twttr import shorten
def main():
    test_twttr()


def test_twttr():
    assert shorten('CS50')=='CS50'
    assert shorten('Twitter')=='Twttr'
    assert shorten("What's your name?")=="Wht's yr nm?"
    assert shorten('PYTHON')=='PYTHN'








if __name__ == "__main__":
    main()
