def main():
    x = input('Greeting: ').upper()
    print(value(x))

def value(greeting):
    if greeting.startswith('HELLO',) or greeting.startswith(' HELLO ',):
        return '$0'
    elif greeting.startswith('H',):
        return '$20'
    else:
        return '$100'



if __name__ == "__main__":
    main()
