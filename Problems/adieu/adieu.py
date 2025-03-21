import inflect
p = inflect.engine()
names = []
while True:
    try:
        people = input()
        x = 0
        names.insert(x,people)
        x = x+1
    except EOFError:
        n = names.reverse()
        #print(n)
        print('Adieu, adieu, to',p.join(names))
        break

