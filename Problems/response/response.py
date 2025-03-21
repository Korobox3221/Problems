import re
import sys
from validator_collection import validators, checkers, errors

def main():
    print(count(input("What's your email address? ")))


def count(s):
    try:
        match = re.search(r'^[a-zA-Z0-9.!#$%&*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$',s)
        if match:
            return 'Valid'
        else:
            return 'Invalid'
    except:
        return 'Invalid'

if __name__ == "__main__":
    main()
