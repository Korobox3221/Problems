def main():
        fraction = input('Fraction: ')
        fraction_converted = convert(fraction)
        output = gauge(fraction_converted)
        print(output)



def convert(fraction):
    while True:
        try:
            ches, delit = fraction.split('/')

            delenie = int(ches) / int(delit)
            if int(delenie) <=1:
                delenie = int(delenie * 100)
                return delenie
            else:
                fraction = input('Fraction: ')
                pass
        except (ValueError, ZeroDivisionError):
            raise




def gauge(z):
    if z >= 99:
        return 'F'
    elif z <= 1:
        return 'E'
    else:
        return f'{z}%'


if __name__ == "__main__":
    main()
