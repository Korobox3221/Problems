Expression = str(input('Expression: '))

x,y,z = Expression.split(' ')
def main():
    add()
    minus()
    multiply()
    divide()


def add():
    if y == '+':
       plus = int(x)+int(z)
       return print(float(plus))



def minus():
    if y == '-':
        min = int(x) - int(z)
        return print(float(min))
def divide():
    if y == '/':
        div = int(x) / int(z)
        return print(float(div))
def multiply():
    if y == '*':
        multi = int(x) * int(z)
        return print(float(multi))

main()
