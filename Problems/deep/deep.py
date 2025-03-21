x = input('What is the Answer to the Great Question of Life, the Universe and Everything? ')

def question():
    if  (x).replace(' ','')== '42':
        print('Yes')
    elif x== 'forty-two':
        print('Yes')
    elif (x).lower()== 'forty two':
        print('Yes')
    else:
        print('No')

question()
