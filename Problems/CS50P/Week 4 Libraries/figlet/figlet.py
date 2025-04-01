from pyfiglet import Figlet
import random
import sys
figlet = Figlet()

try:

    if sys.argv[1] != '-f':
        print('Invalid usage')
        sys.exit(1)
    else: figlet.getFonts()

    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(input()))

except IndexError:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(input()))

