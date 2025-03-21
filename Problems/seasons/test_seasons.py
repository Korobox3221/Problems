from datetime import datetime

from seasons import wordnumbers
import pytest
def main():
    test_valueerror()



def test_valueerror():
    assert wordnumbers("2023-11-22") == "Five hundred twenty-seven thousand forty minutes"


if __name__ == "__main__":
        main()
