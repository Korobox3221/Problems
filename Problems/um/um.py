import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    match = re.findall(r'\b(um)\b',s,re.IGNORECASE)
    #print(match)
    for times in match:
        count = count +1
    return count

if __name__ == "__main__":
    main()
