def main():
    x = input('Input: ')
    print('Output:', shorten(x))



def shorten(word):
    word = word.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','').replace('A','').replace('E','').replace('I','').replace('O','').replace('U','')
    if word == word.lower():
        return word.capitalize()
    elif word == word.upper():
        return word
    else:
        return word



if __name__ == "__main__":
    main()



