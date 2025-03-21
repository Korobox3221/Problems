import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        match = re.search(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', ip)
        if int(match.group(1)) < 256 and int(match.group(2)) < 256 and int(match.group(3)) < 256 and int(match.group(4)) < 256:
            return True
        else:
            return False
    except:
        return False


...


if __name__ == "__main__":
    main()
