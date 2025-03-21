menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
     try:
         direct()










     except (ValueError,EOFError,KeyError):
         print('1')

def direct():
    while True:
        x = input('Item: ').lower()
        for key in menu:
            keynew = key.lower()
            y = menu[key]
            if keynew == x:
                print('Total: ','$',format(y,'.2f') ,sep='')
                x = input('Item: ').lower()
                for key in menu:
                        keynew = key.lower()
                        z = menu[key]
                        if keynew == x:
                            print('Total: ', '$',format(y+z,'.2f'), sep='')
                            x = input('Item: ').lower()
                            for key in menu:
                                    keynew = key.lower()
                                    t = menu[key]
                                    if keynew == x:
                                        print('Total: ', '$',format(y+z+t,'.2f'), sep='')
                                        x = input('Item: ').lower()
                                        for key in menu:
                                                keynew = key.lower()
                                                q = menu[key]
                                                if keynew == x:
                                                    print('Total: ', '$',format(y+z+t+q,'.2f'), sep='')
                                                    x = input('Item: ').lower()
                                                    for key in menu:
                                                            keynew = key.lower()
                                                            w = menu[key]
                                                            if keynew == x:
                                                                print('Total: ', '$',format(y+z+t+q+w,'.2f'), sep='')
                                                                x = input('Item: ').lower()
                                                                for key in menu:
                                                                        keynew = key.lower()
                                                                        e = menu[key]
                                                                        if keynew == x:
                                                                            print('Total: ', '$',format(y+z+t+q+w+e,'.2f'), sep='')

                                                                            x = input('Item: ').lower()
                                                                            for key in menu:
                                                                                    keynew = key.lower()
                                                                                    u = menu[key]
                                                                                    if keynew == x:
                                                                                        print('Total: ', '$',
                                                                                              format(y+z+t+q+w+e+u,'.2f'),
                                                                                              sep='')

                                                                                        x = input('Item: ').lower()
                                                                                        for key in menu:
                                                                                                keynew = key.lower()
                                                                                                i = menu[key]
                                                                                                if keynew == x:
                                                                                                    print('Total: ',
                                                                                                          '$',
                                                                                                          format(y+z+t+q+w+e+u+i,'.2f'),
                                                                                                          sep='')

                                                                                                    x = input(
                                                                                                            'Item: ').lower()
                                                                                                    for key in menu:
                                                                                                            keynew = key.lower()
                                                                                                            p = menu[
                                                                                                                key]
                                                                                                            if keynew == x:
                                                                                                                print(
                                                                                                                    'Total: ',
                                                                                                                    '$',
                                                                                                                    format(y+z+t+q+w+e+u+i+p,'.2f'),
                                                                                                                    sep='')


            #print(y+menu[key])

main()
