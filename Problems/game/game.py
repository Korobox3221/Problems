import random
while True:
        try:
            y = int(input('Level: '))
            if  y > 0:
                break
        except:
            pass
xy = random.randint(1, y)
while True:
            try:
                guess = int(input('Guess: '))
                if guess < xy:
                    print('Too small!')
                elif guess > xy:
                        print('Too large!')
                else:
                        print('Just right!')
                        break
            except:
                    pass
