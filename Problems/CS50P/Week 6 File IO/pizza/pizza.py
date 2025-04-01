import sys
import csv
from tabulate import tabulate
menus = []
def main():
        if sys.argv[2:]:
            print('Too many command-line arguments')
            sys.exit(1)
        try:
            if not sys.argv[1].endswith('.csv'):
                print('Not a CSV file')
                sys.exit(1)
        except IndexError:
            print('Too few command-line arguments')
            sys.exit(1)
        try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    menus.append({'pizza': row[0], 'small': row[1], 'large': row[2]})
            headers = menus[0]
            print(tabulate(menus[1:],headers, tablefmt="grid"))
            #print(menus)
        except FileNotFoundError:
            print('File does not exist')
            sys.exit(1)
        except Exception:
            print('Too many command-line arguments')
            sys.exit(1)

if __name__ == '__main__':
    main()
