import requests
import sys
try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r.json()
    o = r.json()
    bpi = o['bpi']
    USD = bpi['USD']
    rate = USD['rate_float']
    rate = float(sys.argv[1])*float(rate)
    print(f"${rate:,.4f}")
except IndexError:
    print('Missing command-line argument')
    sys.exit(1)
except ValueError:
    print('Command-line argument is not a number')
    sys.exit(1)
