import sys
def main():
        if sys.argv[2:]:
            print('Too many command-line arguments')
            sys.exit(1)
        try:
            if not sys.argv[1].endswith('.py'):
                print('Not a python file')
                sys.exit(1)
        except IndexError:
            print('Too few command-line arguments')
            sys.exit(1)
        try:
            with open(sys.argv[1], 'r') as file:
                #lines = file.readlines()
                count = 0
                buttons = []
                for line in file:
                    buttons.append(line.strip())
            for keys in buttons:
                newkeys = keys.strip()
                if newkeys.startswith('#'):
                    count -=1



            while '' in buttons:
                buttons.remove('')

            for button in buttons:
                    count += 1
            print(count)
        except FileNotFoundError:
            print('File does not exist')
            sys.exit(1)
        except Exception:
            print('Too many command-line arguments')
            sys.exit(1)

if __name__ == '__main__':
    main()
